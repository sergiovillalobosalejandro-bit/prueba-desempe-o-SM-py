from data import inventory, sales
from sales import register_sales, list_sales, load_sales, save_sales
from reports import top_n_sales, sales_by_autor
from validations import ask_int,ask_str, validations
from storage import save_json, load_json
from inventory import list_products, create_product, update_product, delate_product, load_invetory,save_inventory
def menu():
    while True:
        print("""
BIENVENIDO
1. Gestionar inventario (crear/consultar/actualizar/eliminar)
2. Registrar venta
3. Consultar historial de ventas
4. Reportes
5. Guardar datos
6. Cargar datos
0. Salir
""")
        
        options=input("ingresa tu opcion ").strip()

        match options:
            case "1":
                menu_inventory()
            case "2":
                perform_sales()
            case "3":
                list_all_sales()
            case "4":
                menu_reports()
            case "5":
                save_inventory()
                save_sales()
                print("guardado correctamente")
            case "6":
                load_invetory()
                load_sales()
                print("cargado correctamente")
            case "0":
                print("Feliz dia")
                break
            case _:
                print("opcion invalida")

def menu_inventory():
    while True:
        print("""
INVENTARIO
1. Crear producto
2. Consultar todos
3. Actualizar producto
4. Eliminar producto
0. Volver
""")
        
        options= input("ingresa tu opcion ").strip()

        match options:
            case "1":
                while True:
                    titulo=ask_str("Titulo: ")
                    autor = ask_str("Auntor: ")
                    categoria = ask_str("Categoría: ")
                    precio = ask_int("Precio unitario: ", 0)
                    unidad = ask_int("Cantidad en stock: ", 0)
                    create_product(titulo, autor, categoria, precio, unidad)
                    print("Producto creado.")
                    if not validations("deseas agregar otro producto "):
                        break
            case "2":
                for p in list_products():
                    print(p)
            case "3":
                pid= ask_int("ID producto a actualizar ",1)
                titulo=ask_str(("Nuevo titulo "), False)
                autor=ask_str(("Nuevo autor "), False)
                categoria=ask_str(("Nueva categoria "), False)
                precio=input("Nuevo precio ").strip()
                unidad=input("Nuevas unidades ").strip()
                kwargs={}
                if titulo: kwargs["titulo"]=titulo
                if autor: kwargs["autor"]=autor
                if categoria: kwargs["categoria"]=categoria
                if precio.isdigit(): kwargs["precio"]=int(precio)
                if unidad.isdigit(): kwargs["unidad"]=int(unidad)
                if kwargs:
                    ok=update_product(pid, **kwargs)
                    print("Producto actualizado" if ok else "ID no encontrado")
                else:
                    print("canbio cancelado")
            case "4":
                pid=ask_int("ID a eliminar ", 1)
                ok= delate_product(pid)
                print("producto eliminado")
            case "0":
                break
            case _:
                print("opcion invalida")

def perform_sales():
    cliente=ask_str("Nombre del cliente ")
    pid=ask_int("ID de producto ")
    cantidad=ask_int("Cantidad a llevar ")
    try:
        v=register_sales(cliente,pid,cantidad)
        print("Vneta registrada", v)
    except Exception as e:
        print("error", e)

def list_all_sales():
    for v in list_sales():
        print(v)

def menu_reports():
    while True:
        print("""
REPORTES
1. Top 3 productos más vendidos
2. Ventas agrupadas por autor (ingreso por autor)
0. Volver
""")
        
        options=input("ingresa la opcion ")

        match options:
            case "1":
                top=top_n_sales(3)
                for p in top:
                    print(f"{p["titulo"]} - vendidos: {p.get("vendidos",0)}")
            case "2":
                por_autor=sales_by_autor()
                for autor, total in por_autor.items():
                    print(f"{autor}:{total}")
            case "0":
                break
            case _:
                print("opcion invalida")


menu()