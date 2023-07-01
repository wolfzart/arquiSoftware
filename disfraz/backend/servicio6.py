from clients.Service import Service
from database.session import session
from database.models import Usuarios
import json, os, datetime
from time import sleep

class InicioSesion(Service):
    def __init__(self):
        print("Servicio Inicio de sesion")
        super().__init__("INISE")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()
        try:
            print("hola")
            climsg = json.loads(climsg)
            rut = climsg["rut"]
            passw = climsg["contraseña"]
            if db.query(Usuarios).filter(Usuarios.id_rut == rut).first():
                user = db.query(Usuarios).filter(Usuarios.id_rut == rut).first()
                if user.contraseña == passw:
                    db.close()  
                    return "Se Inicio sesion de manera exitosa"
                return "Contraseña Incorrecta"
            db.close()
            return "El usuario no existe"
        except Exception as e:
            db.close()
            return str(e)

def main():
    try:
        InicioSesion()
    except Exception as e:
        print(e)
        sleep(30)
        main()

if __name__ == "__main__":
    main()