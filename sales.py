from typing import Dict,List
from data import  inventory, sales
from inventory import search_id, save_inventory
from storage import save_json, load_json
import datetime

SALES_FILE="sales.json"

def register_sales(cliente:str,producto_id:int,cantidad:int)->Dict:
    producto=search_id(producto_id)
    if producto is None:
        raise ValueError("producto no existe")
    if cantidad <=0:
        raise ValueError("cantidad no valida")
    if producto["unidades"]< cantidad:
        raise ValueError("cantidad de unidades no disponibles")
    
    precio_unidad=producto["precio"]
    subtotal=precio_unidad*cantidad

    venta={
        "id_venta": len(sales)+1,
        "fecha": datetime.datetime.now().isoformat(),
        "cliente": cliente,
        "producto_id": producto_id,
        "producto_nombre": producto["titulo"],
        "autor": producto["autor"],
        "categoria":producto["categoria"],
        "precio_unidad":precio_unidad,
        "subtotal":subtotal
    }


    sales.append(venta)

    producto["unidad"]-= cantidad
    producto["vendidos"]=producto.get("vendidos", 0) + cantidad
    save_inventory()
    save_sales()
    return venta

def save_sales():
    save_json(SALES_FILE,sales)

def load_sales():
    data=load_json(SALES_FILE, None)
    if data is None:
        return
    sales.clear()
    sales.extend(data)

def list_sales()->List[Dict]:
    return sales