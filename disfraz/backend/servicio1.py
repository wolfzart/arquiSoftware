from clients.Service import Service
from database.session import session
from database.models import Prestamo
from database.models import Clientes
import json, os, datetime
from time import sleep
from datetime import date

class Registrar_arriendo(Service):
    def __init__(self):
        print("Servicio de arriendo de disfraces")
        super().__init__("REGAR")
        self.start_service(debug=True)
    
    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()
        try:
            print("hola")
            climsg = json.loads(climsg)
            #prestamo = climsg["id_prest"]
            producto = climsg["id_pro"]
            cantidad = climsg["cant_pro"]


            fecha_prestamo = date(int(climsg["año"]),int(climsg["mes"]),int(climsg["dia"]))
            
            
            nombre_cli = climsg["nom_cli"]
            direccion_cli = climsg["dir_cli"]
            numero_cli = climsg["num_cli"]
            rut_cli = climsg["rut_cli"]
            if not db.query(Clientes).filter(Clientes.id_cli==rut_cli).first():
                #print("hola")
            #if not db.query(Prestamo).filter(Prestamo.id_prestamo == prestamo).first():
                cliente = Clientes(id_cli = rut_cli ,direccion = direccion_cli,nombre = nombre_cli ,telefono = numero_cli )
                db.add(cliente)
                db.commit()
                #db.close()
                #print("22")
                arriendo = Prestamo(id_producto=producto,id_cli=rut_cli,fecha= fecha_prestamo, cantproducto = cantidad, devolucion = False)
                #print("23")
                db.add(arriendo)
                db.commit()
                db.close()
                return 'prestamo realizado'
                print('prestamo realizado')
            else:
                arriendo = Prestamo(id_producto=producto,id_cli=rut_cli,fecha= fecha_prestamo, cantproducto = cantidad, devolucion = False)
                print("23")
                db.add(arriendo)
                db.commit()
                db.close()
                return 'prestamo realizado'
                print('prestamo realizado')
            return "jhasbdhjas" 
        except Exception as e:
            db.close()
            return str(e)
def main():
    try:
        Registrar_arriendo()
    except Exception as e:
        print(e)
        sleep(30)
        main()

if __name__ == "__main__":
    main()
        