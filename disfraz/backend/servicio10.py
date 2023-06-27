from clients.Service import Service
from database.session import session
from database.models import Producto
import json, os, datetime
from time import sleep

class Actualizar_Platillo(Service):
    def __init__(self):
        print("Servicio Modificacion de Stock")
        super().__init__("MODST")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()
        try:
            print("hola")
            climsg = json.loads(climsg)
            id = climsg["id"]
            nombre = climsg["valor"]
            precio = climsg["stock"]
            print("hhh",precio)
            if db.query(Producto).filter(Producto.id_producto == id).first():
                produc = db.query(Producto).filter(Producto.id_producto == id).first()
                produc.nombre=nombre
                total=int(precio)+int(produc.stock)
                if(total>=0):
                    produc.stock=int(precio)+int(produc.stock)
                    db.commit()
                    db.close()
                    return 'Stock actualizado'
                return 'Stock no Actualizado (stock negativo)'    
            else:
                db.close()
                return "El producto no existe"
        except Exception as e:
            db.close()
            return str(e)

def main():
    try:
        Actualizar_Platillo()
    except Exception as e:
        print(e)
        sleep(30)
        main()

if __name__ == "__main__":
    main()
