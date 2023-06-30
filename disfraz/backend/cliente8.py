from clients.Client import Client
from getpass import getpass
import json
        
if __name__ == "__main__":
    print("Cliente Administrar Producto")
    keep_alive = True
    try:
        while(keep_alive):
            valor = input("Registrar(1) o Eliminar(2) Producto: ")
            if valor=="1":
                nombre = input("Ingrese el nombre del producto que se va a registrar: ")
                precio = input("Ingrese el precio del producto: ")
                talla = input("Ingrese la talla de este producto: ")
                stock = input("Ingrese el nuevo stock: ")
            elif valor=="2":
                id = input("Ingrese el id del producto a eliminar: ")
            try: 
                if valor=="1":
                    print("ingrese")
                    climsg = {
                        "nombre": nombre,
                        "valor": valor,
                        "talla": talla,
                        "stock": stock,
                    }
                    a = Client("ADPRO")
                    msg = a.exec_client(debug=True, climsg=json.dumps(climsg))
                    print("###################################\n\n", msg, "\n\n###################################")
                elif valor =="2":
                    print("ingrese2")
                    climsg = {
                        "id": id,
                        "valor": valor,
                    }
                    a = Client("ADPRO")
                    msg = a.exec_client(debug=True, climsg=json.dumps(climsg))
                    print("###################################\n\n", msg, "\n\n###################################")
            except Exception as e:
                print("Error: ", e)
    except KeyboardInterrupt:
        print("\nCerrando cliente, hasta pronto ....")
        keep_alive = False
        exit()