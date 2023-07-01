from clients.Client import Client
from getpass import getpass
import json

#def cliente5(): 
        
if __name__ == "__main__":
    print("Cliente Recepcion Disfraces")
    keep_alive = True
    try:
        while(keep_alive):
            id = input("Ingrese el id del prestamo: ")
            
            try: 
                a = Client("RECDI")
                climsg = {
                    "id": id,
                }
                respuesta = a.exec_client(debug=True, climsg=json.dumps(climsg))
                print("###################################\n\n", respuesta, "\n\n###################################")
            except Exception as e:
                print("Error: ", e)
    except KeyboardInterrupt:
        print("\nCerrando cliente, hasta pronto ....")
        keep_alive = False
        exit()