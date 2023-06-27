from clients.Client import Client
from getpass import getpass
import json
        
if __name__ == "__main__":
    print("Servicio cliente funcionando")
    keep_alive = True
    try:
        while(keep_alive):
            print('Servicio lista de productos')
            input('Presione enter para ver lista de productos...')
            token = ''
            try: 
                a = Client("MOCAT")
                dataCliente = {
                    "token": token,
                }
                respuesta = a.exec_client(debug=True, climsg=json.dumps(dataCliente))
                print("###################################\n\n", respuesta, "\n\n###################################")
                
            except Exception as e:
                print("Error: ", e)
    except KeyboardInterrupt:
        print("\nCerrando cliente, hasta pronto ....")
        keep_alive = False
        exit()