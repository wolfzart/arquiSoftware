from clients.Service import Service
from database.session import session
from database.models import Usuarios
import json, os, datetime
from time import sleep

class AdministrarVendedor(Service):
    def __init__(self):
        print("Servicio Administracion de Vendedores")
        super().__init__("ADVEN")
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
                password = climsg["password"]
                if not db.query(Usuarios).filter(Usuarios.nombre == nombre).first():
                    user = Usuarios(tipo="Vendedor",contraseña=password,nombre=nombre)
                    db.add(user)
                    db.commit()
                    db.close()
                    return 'Nuevo vendedor agregado'
                else:
                    db.close()
                    return "El vendedor ya existe"
            elif valor == "2":
                id_rut = climsg["id_rut"]
                if db.query(Usuarios).filter(Usuarios.id_rut == id_rut).first():
                    user = db.query(Usuarios).filter(Usuarios.id_rut == id_rut).first()
                    db.delete(user)
                    db.commit()
                    db.close()
                    return "Vendedor Eliminado"
                else:
                    db.close()
                    return "El vendedor no existe"
            else:
                db.close()
                return "Opcion invalida"
        except Exception as e:
            db.close()
            return str(e)

def main():
    try:
        AdministrarVendedor()
    except Exception as e:
        print(e)
        sleep(30)
        main()

if __name__ == "__main__":
    main()