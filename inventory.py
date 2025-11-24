from typing import List, Dict, Optional
from data import inventory
from storage import save_json, load_json

INVETARY_FILE="invetory.json"

def obtein_after_id()-> int:
    if not inventory:
        return 1
    return max(p["id"] for p in inventory) + 1

def list_products()-> List[Dict]:
    return inventory

def search_id(pid: int) -> Optional[Dict]:
    return next((p for p in inventory if p["id"] == pid), None)


def create_product(titulo:str, autor: str, categoria:str, precio:int, unidad:int)-> Dict:
    new={
        "id":obtein_after_id(),
        "titulo": titulo,
        "autor":autor,
        "categoria":categoria,
        "precio":precio,
        "unidad": unidad,
        "vendidos": 0
    }
    inventory.append(new)
    return new

def update_product(pid:int, **kwargs)-> bool:
    p=search_id(pid)
    if not p:
        return False
    for k,v in p in kwargs.items():
        if k in p and v is not None:
            p[k]=v
        return True
    
def delate_product(pid:int)-> bool:
    p= search_id(pid)
    if not p:
        return False
    inventory.remove(p)
    return True

def save_inventory():
    save_json(INVETARY_FILE, inventory)

def load_invetory():
    data=load_json(INVETARY_FILE, None)
    if data is None:
        return
    inventory.clear()
    inventory.extend(data)