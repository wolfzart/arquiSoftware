import json, os, datetime
from clients.Service import Service
from database.session import session
from time import sleep
from datetime import date
from database.models import Prestamo
from database.models import Producto

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
            fechaActual = date.today()
            diferencia = fechaActual-rent.fecha
            multa = ((int(prod.precio) * int(rent.cantproducto)) * 0.1) * diferencia.days
            db.close
            print(multa)
            return str(int(multa))
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