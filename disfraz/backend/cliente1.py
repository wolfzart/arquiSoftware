from clients.Client import Client
from getpass import getpass
import json

#def cliente1(): 

if __name__ == "__main__":
    print("cliente registrar prestamos")
    keep_alive =True
    try:
        while(keep_alive):
            id_producto = input("Ingrese el id del producto: ")
            cantproducto = input("Ingrese la cantidad del producto: ")
            print("Ingrese fecha de entrega\n")
            
            dia = input("ingrese dia: ")
            mes = input("Ingrese mes: ")
            año = input ("ingrese año: ")

            id_rut_cliente  = input("Ingrese el rut del cliente: ")
            direccion_cliente  = input("Ingrese la direccion del cliente: ")
            nombre_cliente  = input("Ingrese el nombre del cliente: ")
            numero_cliente  = input("Ingrese el numero de telefono del cliente: ")
            try: 
                print("ingrese")
                climsg = {
                    "id_pro": id_producto,
                    "cant_pro": cantproducto ,
                    "dia": dia,
                    "mes": mes,
                    "año": año,
                    #"fecha": fecha,
                    "rut_cli": id_rut_cliente,
                    "dir_cli": direccion_cliente,
                    "nom_cli": nombre_cliente,
                    "num_cli": numero_cliente,
                    }
                a = Client("REGAR")
                msg = a.exec_client(debug=True, climsg=json.dumps(climsg))
                print("###################################\n\n", msg, "\n\n###################################")   
            except Exception as e:
                print("Error: ", e)
    except KeyboardInterrupt:
        print("\nCerrando cliente, hasta pronto ....")
        keep_alive = False
        exit()  
