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
            prestamo = climsg["id_prest"]
            producto = climsg["id_producto"]
            cantidad = climsg["cantproducto"]
            fecha_prestamo = climsg["fecha"]
            nombre_cli = climsg["nombre_cliente"]
            direccion_cli = climsg["direccion_cliente"]
            numero_cli = climsg["numero_cliente"]
            rut_cli = climsg["id_rut_cliente"]
            if not db.query(Prestamo).filter(Prestamo.id_prestamo == prestamo).first():
                cliente = Clientes(id_cli= rut_cli ,direccion = direccion_cli,nombre=nombre_cli ,telefono=  numero_cli )
                db.add(cliente)
                db.commit()
                db.close()
                arriendo = Prestamo(id_producto=producto,id_cli=rut_cli,fecha= fecha_prestamo, cantproducto= cantidad)
                db.add(arriendo)
                db.commit()
                db.close()
                return 'prestamo realizado'
            else:
                    db.close()
                    return "error"
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
        
