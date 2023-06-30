from clients.Client import Client
from getpass import getpass
from datetime import date
import json
        
if __name__ == "__main__":
    print("Cliente Modificar Stock")
    keep_alive = True
    try:
        while(keep_alive):
            rut = input("Ingrese nombre de rut: ")
            password = input("Ingrese contraseña: ")
            try: 
            
                print("ingrese")
                climsg = {
                    "rut": rut,
                    "contraseña": password,
                }
                a = Client("INISE")
                msg = a.exec_client(debug=True, climsg=json.dumps(climsg))
                print("###################################\n\n", msg, "\n\n###################################")
            
            except Exception as e:
                print("Error: ", e)
    except KeyboardInterrupt:
        print("\nCerrando cliente, hasta pronto ....")
        keep_alive = False
        exit()