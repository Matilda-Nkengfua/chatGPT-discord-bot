import json
from app.dev_backend.filepath import SearchFile

def read_json(filename):
    filepath=SearchFile(filename).completePath()
    with open(filepath, 'r', encoding="utf8") as file:
        return json.load(file)