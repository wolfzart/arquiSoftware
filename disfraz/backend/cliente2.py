from clients.Client import Client
from getpass import getpass
from datetime import date
import json

#def cliente2():    
if __name__ == "__main__":
    print("Cliente Extender Arriendo")
    keep_alive = True
    try:
        while(keep_alive):
            #fecha = input("Ingrese la nueva fecha de arriendo: ")
            print("Ingrese fecha de entrega\n")
            
            dia = input("ingrese dia: ")
            mes = input("Ingrese mes: ")
            año = input ("ingrese año: ")
            id_prestamo = input("Ingrese el id del prestamo que se debe modificar: ")
            #fecha = date(int(año),int(mes),int(dia))
            try: 
                climsg = {
                    #"fecha": fecha,
                    "dia": dia,
                    "mes": mes,
                    "año": año,
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