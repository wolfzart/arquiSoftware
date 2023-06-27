from clients.Client import Client
from getpass import getpass
import json
        
if __name__ == "__main__":
    print("Cliente Modificar Stock")
    keep_alive = True
    try:
        while(keep_alive):
            id = input("Ingrese el id del producto que se modificara el stock: ")
            valor = input("Agregar(1) o disminuir stock(2): ")
            stock = input("Ingrese el nuevo stock: ")
            
            try: 
                if valor=="1":
                    print("ingrese")
                    climsg = {
                        "id": id,
                        "valor": valor,
                        "stock": stock,
                    }
                    a = Client("MODST")
                    msg = a.exec_client(debug=True, climsg=json.dumps(climsg))
                    print("###################################\n\n", msg, "\n\n###################################")
                elif valor =="2":
                    print("ingrese2")
                    climsg = {
                        "id": id,
                        "valor": valor,
                        "stock": -int(stock)
                    }
                    a = Client("MODST")
                    msg = a.exec_client(debug=True, climsg=json.dumps(climsg))
                    print("###################################\n\n", msg, "\n\n###################################")
            except Exception as e:
                print("Error: ", e)
    except KeyboardInterrupt:
        print("\nCerrando cliente, hasta pronto ....")
        keep_alive = False
        exit()