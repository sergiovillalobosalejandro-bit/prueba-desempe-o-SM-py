from typing import Dict, List
from data import inventory,sales
from collections import Counter, defaultdict



def top_n_sales(n=3)->List[Dict]:
    if not inventory:
        return []
    store_by_sales=sorted(inventory, key=lambda p:p.get("vendidos",0), reverse=True)
    return store_by_sales[:n]

def sales_by_autor()->Dict[str, float]:
    ag=defaultdict(ag)
    for v in sales:
        ag[v["autor"]] += v["subtotal"]
        return dict(ag)
    
