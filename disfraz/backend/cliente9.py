from clients.Client import Client
from getpass import getpass
import json
        
if __name__ == "__main__":
    print("Cliente Administrar Vendedores")
    keep_alive = True
    try:
        while(keep_alive):
            valor = input("Registrar(1) o Eliminar(2) un Vendedor: ")
            if valor=="1":
                nombre = input("Ingrese el nombre del vendedor que se va a registrar: ")
                password = input("Ingrese la contraseña del usuario: ")
            elif valor=="2":
                id_rut = input("Ingrese el id del vendedor a eliminar: ")
            try: 
                if valor=="1":
                    print("ingrese")
                    climsg = {
                        "nombre": nombre,
                        "valor": valor,
                        "password": password,
                    }
                    a = Client("ADVEN")
                    msg = a.exec_client(debug=True, climsg=json.dumps(climsg))
                    print("###################################\n\n", msg, "\n\n###################################")
                elif valor =="2":
                    print("ingrese2")
                    climsg = {
                        "id_rut": id,
                        "valor": valor,
                    }
                    a = Client("ADVEN")
                    msg = a.exec_client(debug=True, climsg=json.dumps(climsg))
                    print("###################################\n\n", msg, "\n\n###################################")
            except Exception as e:
                print("Error: ", e)
    except KeyboardInterrupt:
        print("\nCerrando cliente, hasta pronto ....")
        keep_alive = False
        exit()