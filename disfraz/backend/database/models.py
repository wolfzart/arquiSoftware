import json
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Date
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id_rut = Column(Integer, primary_key=True)
    tipo = Column(String, nullable=False)
    contraseña = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    historiales = relationship("Historial", back_populates="usuario")
    def __repr__(self):
        return '<Usuario %r>' % self.name

class Producto(Base):
    __tablename__ = "producto"
    id_producto = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    precio = Column(Integer, nullable=False)
    talla = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
    def __repr__(self):
        return '<Producto %r>' % self.name

class Clientes(Base):
    __tablename__ = 'clientes'
    id_cli = Column(Integer, primary_key=True)
    direccion = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    def __repr__(self):
        return '<Clientes %r>' % self.name


class Historial(Base):
    __tablename__ = 'historial'
    id_historial = Column(Integer, primary_key=True)
    id_rut = Column(Integer, ForeignKey('usuarios.id_rut'), nullable=False)
    id_prestamo = Column(Integer, ForeignKey('prestamo.id_prestamo'), nullable=False)
    id_cli = Column(Integer, ForeignKey('clientes.id_cli'), nullable=False)
    multa = Column(Integer, nullable=False)
    pagado = Column(Boolean, nullable=False)
    usuario = relationship("Usuarios", back_populates="historiales")
    prestamo = relationship("Prestamo", back_populates="historial")
    def __repr__(self):
        return '<Historial %r>' % self.name
class Prestamo(Base):
    __tablename__ = 'prestamo'
    id_prestamo = Column(Integer, primary_key=True)
    id_producto = Column(Integer, ForeignKey('Producto.id_producto'), nullable=False)
    id_cli = Column(Integer, ForeignKey('Clientes.id_cli'), nullable=False)
    fecha = Column(Date, nullable=False)
    cantproducto = Column(Integer, nullable=False)
    devolucion = Column(Boolean, nullable=False)
    historial = relationship("Historial", back_populates="prestamo")
    def __repr__(self):
        return '<Prestamo %r>' % self.name


'''    
class Usuario(Base):
    __tablename__ = 'usuarios'
    id_rut = Column(Integer, primary_key=True)
    tipo = Column(String, nullable=False)
    contraseña = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    historiales = relationship("Historial", back_populates="usuario")
    def __repr__(self):
        return '<Usuario %r>' % self.name

class Historial(Base):
    __tablename__ = 'historial'
    id_Historial = Column(Integer, primary_key=True)
    id_rut = Column(Integer, ForeignKey('usuarios.id_rut'), nullable=False)
    id_prestamo = Column(Integer, ForeignKey('prestamo.id_prestamo'), nullable=False)
    multa = Column(Integer, nullable=False)
    usuario = relationship("Usuario", back_populates="historiales")
    prestamo = relationship("Prestamo", back_populates="historial")
    def __repr__(self):
        return '<Historial %r>' % self.name

class Prestamo(Base):
    __tablename__ = 'prestamo'
    id_prestamo = Column(Integer, primary_key=True)
    id_producto = Column(String, ForeignKey('producto.id_producto'), nullable=False)
    fecha = Column(Date, nullable=False)
    canproducto = Column(Integer, nullable=False)
    direccion = Column(String, nullable=False)
    nombre_cliente = Column(String, nullable=False)
    numero_cliente = Column(String, nullable=False)
    historial = relationship("Historial", back_populates="prestamo")
    producto = relationship("Producto", back_populates="prestamos")
    def __repr__(self):
        return '<Prestamo %r>' % self.name

class Producto(Base):
    __tablename__ = 'producto'
    id_producto = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    precio = Column(Integer, ForeignKey('historial.id_prestamo'), nullable=False)
    talla = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
    prestamos = relationship("Prestamo", back_populates="producto")
    def __repr__(self):
        return '<Producto %r>' % self.name
    
class Platillos(Base):
    __tablename__ = 'platillo'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=True)
    precio = Column(Integer, nullable=True)
    stock = Column(Integer, nullable=True)
    def __repr__(self):
        return '<Platillo %r>' % self.name

class Miembro(Base):
    __tablename__ = 'miembro'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey(
        'usuario.id'), nullable=False)
    usuario = relationship('Usuario', back_populates='miembro')
    rol = Column(String(80), nullable=False)
    admin = Column(Boolean, nullable=False)
    publicaciones = relationship(
        'Publicacion', back_populates='miembro', lazy='dynamic')
    join_date = Column(Date, nullable=True)
    grupo_id = Column(Integer, ForeignKey(
        'grupo.id'), nullable=True)
    grupo = relationship('Grupo', back_populates='miembro')
    def __repr__(self):
        return '<Miembro %r>' % self.usuario_id

class Grupo(Base):
    __tablename__ = 'grupo'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(80), nullable=False)
    descripcion = Column(String(80), nullable=False)
    miembro = relationship('Miembro', back_populates='grupo', lazy=True)

    def __repr__(self):
        return '<Grupo %r>' % self.name

class Evento(Base):
    __tablename__ = 'evento'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(80), nullable=False)
    descripcion = Column(String(256), nullable=False)
    fecha_inicio = Column(String(256), nullable=False)
    fecha_fin = Column(String(256), nullable=False)
    usuario_id = Column(Integer, ForeignKey(
        'usuario.id'), nullable=False)
    grupo_id = Column(Integer, ForeignKey(
        'grupo.id'), nullable=True)
    def __repr__(self):
        return '<Evento %r>' % self.nombre

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), nullable=True)
    password = Column(String(256), nullable=False)
    email = Column(String(80), nullable=False)
    phone = Column(String(10), nullable=True)
    fecha_ingreso = Column(Date, nullable=True)
    miembro = relationship('Miembro', back_populates='usuario')
    amistad = relationship('Amistad', back_populates='usuario')
    def __repr__(self):
        return '<Usuario %r>' % self.name

class Publicacion(Base):
    __tablename__ = 'publicacion'
    id = Column(Integer, primary_key=True)
    miembro_id = Column(Integer, ForeignKey(
        'miembro.id'), nullable=False)
    miembro = relationship('Miembro', back_populates='publicaciones')
    titulo = Column(String(80), nullable=False)
    descripcion = Column(String(256), nullable=True)
    create_date = Column(Date, nullable=True)
    def __repr__(self):
        return '<Publicacion %r>' % self.contenido

        
class Amistad(Base):
    __tablename__ = 'amistad'
    usuario_id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)
    usuario = relationship('Usuario', back_populates='amistad')
    amigo_id = Column(Integer, nullable=False)

    def __repr__(self):
        return '<Amistad %r>' % self.usuario_id
'''
def to_dict(obj):
    if isinstance(obj.__class__, DeclarativeMeta):
        # an SQLAlchemy class
        fields = {}
        for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
            data = obj.__getattribute__(field)
            try:
                # this will fail on non-encodable values, like other classes
                json.dumps(data)
                if data is not None:
                    fields[field] = data
            except TypeError:
                pass
        # a json-encodable dict
        return fields