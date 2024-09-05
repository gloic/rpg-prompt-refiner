from src.entity.character import Character
from src.llm.llm import Llm


class Evaluation:
    def __init__(self, params: None, llm: Llm = None):
        self.params = params or {}
        self.system_prompt_character_skyrim = self.params.get('system_prompt_character_skyrim', None)
        self.system_prompt_character_evaluation = self.params.get('system_prompt_character_evaluation', None)
        self.user_prompt_character_evaluation = self.params.get('user_prompt_character_evaluation', None)
        self.prompts_evals = self.params.get('prompt_eval', None)

        self.llm = llm

    def generate_conversation(self, character: Character, user_prompts):
        get_history_entry = lambda role, content: {"role": role, "content": content}

        system_prompt = self.system_prompt_character_skyrim.format(
            name=character.get_name(),
            bio=character.get_new_prompt(),
            trust="étranger",
            location="Blancherive",
            language="French",
            time="10:04",
            time_group="",
            conversation_summary=""
        )

        history = [get_history_entry("system", system_prompt)]

        for user_prompt in user_prompts:
            if user_prompt is not None and user_prompt != "":
                print(" - joueur: " + user_prompt)
                history.append(get_history_entry("user", user_prompt))

            response = self.llm.generate(history, temperature=1, top_p=0.9)

            print(" - " + character.get_name() + ": " + response)
            history.append(get_history_entry(character.get_name(), response))

        return history

    def evaluate(self, character: Character):
        print("******")
        print("SIMULATION")
        print("******")
        for user_prompts in self.prompts_evals:

            history = []
            for chat in self.generate_conversation(character, user_prompts):
                history.append("-{role}: {content}".format(role=chat["role"],
                                                           content=chat["content"]))

            print("> Evaluation")

            response_eval = self.llm.generate(system_prompt=self.system_prompt_character_evaluation.format(name=character.get_name()),
                                              prompt=self.user_prompt_character_evaluation.format(bio=character.get_new_prompt(), chat_history=history),
                                              temperature=0.9,
                                              top_p=0.8)
            print(response_eval)
            return {
                'eval': response_eval,
                'history': history
            }
