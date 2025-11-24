import json
from typing import List, Dict

def save_json(path:str,data)-> None:
    with open (path,"w", newline="", encoding="utf-8") as file:
        json.dump(data,file,ensure_ascii=False, indent=4)

def load_json(path:str, default):
    try:
        with open(path,"r",newline="", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return default
    except Exception:
        return default