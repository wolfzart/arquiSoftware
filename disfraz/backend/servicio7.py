from clients.Service import Service
from database.session import session
from database.models import Prestamo,Producto, to_dict
import json, sys, os, datetime
from time import sleep

class PrestamosActuales(Service):
    def __init__(self):
        print("Servicio para ver Lista de prestamos")
        super().__init__("PREAC")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()
        try:
            climsg = json.loads(climsg)
            #token = climsg["token"]
           # decoded = jwt.decode(
            #    token, os.environ['SECRET_KEY'], algorithms=['HS256'])
            platillos = []
            for pres in db.query(Prestamo).all():
                platillos.append(to_dict(pres))
            if platillos:
                output = "----------------------------------------------------\n"
                n=0
                for pres in platillos:
                    if(n>0):
                        print(pres)
                        output += "ID: "+str(pres["id_prestamo"])+"\n"
                        if db.query(Producto).filter(Producto.id_producto ==pres["id_producto"]).first():
                            produc=db.query(Producto).filter(Producto.id_producto ==pres["id_producto"]).first()
                            nombreProducto= produc.nombre
                            output += "Disfraz: "+nombreProducto+"\n"

                        output += "----------------------------------------------------\n"
                    # replace 0xde
                    n=n+1 
                
                    prod = []
                    '''for productos in db.query(Producto).filter(Producto.id_producto ==pres["id_producto"]).first():
                        prod.append(to_dict(producto))
                    if prod:
                        n1>0
                        for productos in prod:
                            if(n>0):
                                print("aqui")
                                print(productos)
                            n=n+1
                    '''
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
        PrestamosActuales()
    except Exception as e:
        print(e)
        sleep(30)
        main()

if __name__ == "__main__":
    main()

