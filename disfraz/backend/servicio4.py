from clients.Service import Service
from database.session import session
from database.models import Producto, to_dict
import json, sys, os, datetime
from time import sleep

class MostrarProductos(Service):
    def __init__(self):
        print("Servicio para ver Lista de productos")
        super().__init__("MOCAT")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()
        try:
            climsg = json.loads(climsg)
            #token = climsg["token"]
           # decoded = jwt.decode(
            #    token, os.environ['SECRET_KEY'], algorithms=['HS256'])

            '''
            id_producto INTEGER NOT NULL,
            nombre VARCHAR NOT NULL,
            precio INTEGER NOT NULL,
            talla INTEGER NOT NULL,
            stock INTEGER NOT NULL,

            id_producto = Column(Integer, primary_key=True)
            nombre = Column(String, nullable=False)
            precio = Column(Integer, nullable=False)
            talla = Column(Integer, nullable=False)
            stock = Column(Integer, nullable=False)
            '''
            prs = []
            print("hola")
            #print(Producto)
            for prod in db.query(Producto).all():
                prs.append(to_dict(prod))
            if prs:
                output = "----------------------------------------------------\n"
                for prod in prs:
                    print("intento")
                    output += "ID: "+str(prod["id_producto"])+"\n"
                    output += "Disfraz: "+prod["nombre"]+"\n"
                    output += "Precio: "+str(prod["precio"])+"\n"
                    output += "talla: "+str(prod["talla"])+"\n"
                    output += "Stock: "+str(prod["stock"])+"\n"
                    output += "----------------------------------------------------\n"
                # replace 0xde 
                output = output.replace("\xde", "")
                return (output)
            else:
                return "No hay platillos inscritos"
                    
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            return "Error: " + str(e) + " " + fname + " " + str(exc_tb.tb_lineno)

def main():
    try:
        MostrarProductos()
    except Exception as e:
        print(e)
        sleep(30)
        main()

if __name__ == "__main__":
    main()

