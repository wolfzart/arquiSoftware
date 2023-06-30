from clients.Service import Service
from database.session import session
from database.models import Prestamo
import json, os, datetime
from time import sleep
from datetime import date

class ExtenderArriendo(Service):
    def __init__(self):
        print("Servicio de Extension de Arriendos")
        super().__init__("EXARR")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()
        try:
            print("hola")
            climsg = json.loads(climsg)
            fecha = climsg["fecha"]
            id_prestamo = climsg["id_prestamo"]
            if db.query(Prestamo).filter(Prestamo.id_prestamo == id_prestamo).first():
                rent = db.query(Prestamo).filter(Prestamo.id_prestamo == id_prestamo).first()
                if(datetime.strptime(fecha, '%y/%m/%d') >= date.today()):
                    rent.fecha = fecha
                    db.commit()
                    db.close()
                    return 'Fecha actualizada'
                else:
                    db.close()
                    return 'Fecha no Actualizada (fecha anterior a la fecha actual)'    
            else:
                db.close()
                return "El prestamo no existe"
        except Exception as e:
            db.close()
            return str(e)

def main():
    try:
        ExtenderArriendo()
    except Exception as e:
        print(e)
        sleep(30)
        main()

if __name__ == "__main__":
    main()
