import argparse
import json
import os
from os.path import join

import gradio as gr
from openai import OpenAI

os.environ['GRADIO_ANALYTICS_ENABLED'] = 'False'
os.environ["no_proxy"] = "localhost,127.0.0.1,::1"
os.environ['NO_PROXY'] = "localhost,127.0.0.1,::1"


def load_config(config_file):
    with open(config_file, "r") as file:
        json_data = json.load(file)
    return json_data


def predict(message, history):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human})
        history_openai_format.append({"role": "assistant", "content": assistant})
    history_openai_format.append({"role": "user", "content": message})

    response = client.chat.completions.create(model='osef',
                                              messages=history_openai_format,
                                              temperature=1.0,
                                              stream=True)

    partial_message = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            partial_message = partial_message + chunk.choices[0].delta.content
            yield partial_message


def gradio_interface():
    gr.ChatInterface(
        analytics_enabled=False,
        fn=predict
    ).launch()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RP")
    parser.add_argument("--config", default="default.json", help="Path to JSON config file in the configs folder")
    args = parser.parse_args()

    config_path = join("rp_test/configs", args.config)
    config = load_config(config_path)

    client = OpenAI(
        api_key="DEV",
        base_url="http://127.0.0.1:5000/v1"
    )


# if args.gui:
    gradio_interface()
    # else:
    #     run_process(config)
