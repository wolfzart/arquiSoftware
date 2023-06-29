from clients.Client import Client
from getpass import getpass
import json
        
if __name__ == "__main__":
    print("Cliente Extender Arriendo")
    keep_alive = True
    try:
        while(keep_alive):
            fecha = input("Ingrese la nueva fecha de arriendo: ")
            id_prestamo = input("Ingrese el id del prestamo que se debe modificar: ")
            
            try: 
                climsg = {
                    "fecha": fecha,
                    "id_prestamo": id_prestamo,
                }
                a = Client("EXARR")
                msg = a.exec_client(debug=True, climsg=json.dumps(climsg))
                print("###################################\n\n", msg, "\n\n###################################")
            except Exception as e:
                print("Error: ", e)
    except KeyboardInterrupt:
        print("\nCerrando cliente, hasta pronto ....")
        keep_alive = False
        exit()