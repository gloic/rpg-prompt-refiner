from openai import OpenAI


class Llm:

    def __init__(self, params: None):
        self.params = params or {}
        self.base_url = self.params.get('base_url', None)
        self.api_key = self.params.get('api_key', None)
        self.temperature = self.params.get('temperature', 0.7)
        self.top_p = self.params.get('top_p', 0.9)

        self.llm = OpenAI(base_url=self.base_url, api_key=self.api_key)

    def build_messages(self, system_prompt: str = None, user_prompt: str = None):
        return [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

    def generate(self, messages=None, system_prompt: str = None, prompt: str = None, temperature: float = None, top_p: float = None):

        if messages is None:
            history = self.build_messages(system_prompt, prompt)
        else:
            history = messages

        temp = temperature or self.temperature
        p = top_p or self.top_p

        completion = self.llm.chat.completions.create(
            model="osef",
            messages=history,
            temperature=temp,
            top_p=p,
        )
        response = completion.choices[0].message.content
        return response
