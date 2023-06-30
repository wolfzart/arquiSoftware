from clients.Service import Service
from database.session import session
from database.models import Producto
import json, os, datetime
from time import sleep

class AdministrarProducto(Service):
    def __init__(self):
        print("Servicio Administracion de Productos")
        super().__init__("ADPRO")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()
        try:
            print("hola")
            climsg = json.loads(climsg)
            valor = climsg["valor"]
            if valor == "1":
                nombre = climsg["nombre"]
                precio = climsg["precio"]
                talla = climsg["talla"]
                stock = climsg["stock"]
                prod = Producto(nombre=nombre,precio=precio,talla=talla,stock=stock)
                db.add(prod)
                db.commit()
                db.close()
                return 'Nuevo producto agregado en el catalogo'    
            elif valor == "2":
                id = climsg["id"]
                if db.query(Producto).filter(Producto.id_producto == id).first():
                    prod = db.query(Producto).filter(Producto.id_producto == id).first()
                    db.delete(prod)
                    db.commit()
                    db.close()
                    return "Producto Eliminado"
                else:
                    db.close()
                    return "El producto no existe"
            else:
                db.close()
                return "Opcion invalida"
        except Exception as e:
            db.close()
            return str(e)

def main():
    try:
        AdministrarProducto()
    except Exception as e:
        print(e)
        sleep(30)
        main()

if __name__ == "__main__":
    main()
