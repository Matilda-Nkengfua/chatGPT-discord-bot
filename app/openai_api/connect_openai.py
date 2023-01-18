from dotenv import load_dotenv
import openai
import os
from app.dev_backend.utils import read_json

load_dotenv()

openai.api_key = os.getenv("OPENAI_APIKEY")
config = read_json("config.json")


def chatgpt_response(prompt):
    response = openai.Completion.create(
        engine=config["ai_models"]["davinci"], prompt=prompt, temperature=0.75, max_tokens=100
    )
    # response dictionary keys: ['id', 'object', 'created', 'model', 'choices', 'usage']
    res_dict = response.get("choices")
    if res_dict and len(res_dict) > 0:
        prompt_response = res_dict[0]["text"]
    return prompt_response
