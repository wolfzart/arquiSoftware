from clients.Service import Service
from database.session import session
from database.models import Prestamo, Producto
from clients.Client import Client
from getpass import getpass
import json, os, datetime
from time import sleep
from datetime import date

class RecepcionDisfraces(Service):
    def __init__(self):
        print("Servicio Recepcion de Disfraces")
        super().__init__("RECDI")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()
        try:
            print("hola")
            climsg = json.loads(climsg)
            id = climsg["id"]
            if db.query(Prestamo).filter(Prestamo.id_prestamo == id).first():
                rent = db.query(Prestamo).filter(Prestamo.id_prestamo == id).first()
                if date.today() <= datetime.strptime(rent.fecha, '%y/%m/%d'):
                    prod = db.query(Producto).filter(Producto.id_producto == rent.id_producto).first()
                    monto = int(prod.precio) * int(rent.cantproducto)
                    return monto
                else:
                    a = Client("MULTA")
                    dataCliente = {
                        "id": id,
                    }
                    multa = a.exec_client(debug=True, climsg=json.dumps(dataCliente))
                    prod = db.query(Producto).filter(Producto.id_producto == rent.id_producto).first()
                    monto = multa + (int(prod.precio) * int(rent.cantproducto))
                    return monto
                    
            else:
                db.close()
                print("No existe un prestamo con esta id")
                return 0
        except Exception as e:
            db.close()
            return str(e)

def main():
    try:
        RecepcionDisfraces()
    except Exception as e:
        print(e)
        sleep(30)
        main()

if __name__ == "__main__":
    main()