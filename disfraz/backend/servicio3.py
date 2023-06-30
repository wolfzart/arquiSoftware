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
        print("Servicio de Multas")
        super().__init__("MULTA")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()
        try:
            print("hola")
            climsg = json.loads(climsg)
            id = climsg["id"]
            rent = db.query(Prestamo).filter(Prestamo.id_prestamo == id).first()
            prod = db.query(Producto).filter(Producto.id_producto == rent.id_producto).first()
            plannedDay = date.today().day
            deliverDay = datetime.strptime(rent.fecha, '%y/%m/%d').day
            days = deliverDay - plannedDay
            multa = ((int(prod.precio) * int(rent.cantproducto)) * 0.1) * days
            return multa
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