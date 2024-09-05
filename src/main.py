import os

import pandas as pd

from src.entity.character import Character
from src.llm.llm import Llm
from src.utils.config_loader import ConfigLoader
from src.workflow.creation import Creation
from src.workflow.evaluation import Evaluation
from src.utils.csv_file_manager import CsvFileManager

os.environ["no_proxy"] = "192.168.*,localhost,127.0.0.1,::1"

data = pd.read_csv('../data/skyrim_characters_fr.csv')

def run(config):
    llm_params = config.get("llm", {}).get("params", {})
    creation_params = config.get("creation", {}).get("params", {})
    eval_params = config.get("evaluation", {}).get("params", {})

    llm = Llm(llm_params)

    creation = Creation(creation_params, llm)
    evaluation = Evaluation(eval_params, llm)

    i = 0
    for i, row in data.sample(replace=True, frac=1).iterrows():
        print("*********")

        character_data = {
            'name': row['name'],
            'race': row['race'],
            'gender': row['gender'],
            'species': row['species'],
            'bio': row['bio']
        }

        character = Character(**character_data)
        new_prompt = creation.generate_prompt_character(character)
        character.set_new_prompt(new_prompt)
        print(character.get_new_prompt())

        response_eval = evaluation.evaluate(character)

        csv_file_manager = CsvFileManager("../../data/samples.csv", ["col1", "col2"])
        csv_file_manager.add_line_csv(col1=history, col2=response_eval)
        csv_file_manager.save_csv()

        if i > 2:
            break


if __name__ == "__main__":
    config = ConfigLoader().load_config()
    run(config)