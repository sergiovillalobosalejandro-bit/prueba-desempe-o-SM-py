def ask_int(prompt: str, min:int=None)-> int:
    while True:
        val=input(prompt).strip()
        if not val.isdigit():
            print("ingrese un valor valido")
            continue
        num=int(val)

        if min is not None and num < min:
            print(f"ingresa un numero mayor o igual a {min}")
            continue
        return num
    
def ask_str(prompt: str, mandatory: bool=True)-> str:
    while True:
        val=input(prompt).strip()
        if mandatory and not val:
            print("valor no valido")
            continue
        return val
    

def validations(mensaje:str)-> str:
    while True:
        confirmation=input(mensaje)

        if confirmation=="si":
            return True
        elif confirmation=="no":
            return False
        else:
            print("valor no valido contesta con un si o no")
