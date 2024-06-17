from sqlalchemy import Column, Integer, String, Date, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class Habitacion(Base):
    __tablename__ = 'habitacion'

    idhabitacion = Column(Integer, primary_key=True)
    numero_habitacion = Column(Integer)
    tipo_habitacion = Column(String)
    precio = Column(Integer)

    reservas = relationship("Reserva")
    
    # Métodos estáticos para operaciones CRUD
    @staticmethod
    def agregar_habitacion(session, numero_habitacion, tipo_habitacion, precio):
        nueva_habitacion = Habitacion(numero_habitacion=numero_habitacion, tipo_habitacion=tipo_habitacion, precio=precio)
        session.add(nueva_habitacion)
        session.commit()
        print("Habitacion agregada correctamente")

    @staticmethod
    def modificar_habitacion(session, id_habitacion, **kwargs):
        habitacion = session.query(Habitacion).filter_by(idhabitacion=id_habitacion).first()
        if habitacion:
            for key, value in kwargs.items():
                setattr(habitacion, key, value)
            session.commit()
            print("Habitacion actualizada")
        else:
            print("Habitacion no encontrada")

    @staticmethod
    def eliminar_habitacion(session, id_habitacion):
        habitacion = session.query(Habitacion).filter_by(idhabitacion=id_habitacion).first()
        if habitacion:
            session.delete(habitacion)
            session.commit()
            print("Habitacion eliminada correctamente")
        else:
            print("Habitacion no encontrada")

class Reserva(Base):
    __tablename__ = 'reserva'

    idreserva = Column(Integer, primary_key=True)
    fecha_reserva = Column(Date)
    fecha_llegada = Column(Date)
    fecha_salida = Column(Date)
    estado_reserva = Column(String)
    idcliente = Column(Integer, ForeignKey('cliente.idcliente'))
    idhabitacion = Column(Integer, ForeignKey('habitacion.idhabitacion'))
    
    cliente = relationship('Cliente', back_populates='reservas', overlaps="cliente")

    habitacion = relationship('Habitacion', back_populates='reservas', overlaps="reservas")
    # Métodos estáticos para operaciones CRUD
    @staticmethod
    def agregar_reserva(session, fecha_reserva, fecha_llegada, fecha_salida, estado_reserva, id_cliente, id_habitacion):
        nueva_reserva = Reserva(fecha_reserva=fecha_reserva, fecha_llegada=fecha_llegada, fecha_salida=fecha_salida, estado_reserva=estado_reserva, idcliente=id_cliente, idhabitacion=id_habitacion)
        session.add(nueva_reserva)
        session.commit()
        print("Reserva agregada correctamente")

    @staticmethod
    def modificar_reserva(session, id_reserva, **kwargs):
        reserva = session.query(Reserva).filter_by(idreserva=id_reserva).first()
        if reserva:
            for key, value in kwargs.items():
                setattr(reserva, key, value)
            session.commit()
            print("Reserva actualizada")
        else:
            print("Reserva no encontrada")

    @staticmethod
    def eliminar_reserva(session, id_reserva):
        reserva = session.query(Reserva).filter_by(idreserva=id_reserva).first()
        if reserva:
            session.delete(reserva)
            session.commit()
            print("Reserva eliminada correctamente")
        else:
            print("Reserva no encontrada")

    @staticmethod
    def cancelar_reserva(session, id_reserva):
        reserva_cancelar = session.query(Reserva).filter_by(idreserva=id_reserva).first()
        if reserva_cancelar:
            reserva_cancelar.estado_reserva = "Cancelada"
            session.commit()
            print("Reserva cancelada exitosamente.")
        else:
            print("La reserva no existe en el sistema.")

class Cliente(Base):
    __tablename__ = 'cliente'

    idcliente = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    direccion = Column(String)
    num_pasaporte = Column(String)
    reservas = relationship("Reserva")

    @staticmethod
    def agregar_cliente(session, nombre, apellido, direccion, num_pasaporte):
        nuevo_cliente = Cliente(nombre=nombre, apellido=apellido, direccion=direccion, num_pasaporte=num_pasaporte)
        session.add(nuevo_cliente)
        session.flush()  
        print("ID del Cliente generado:", nuevo_cliente.idcliente)
        session.commit()
        print("Cliente agregado correctamente")

    @staticmethod
    def modificar_cliente(session, id_cliente, **kwargs):
        cliente = session.query(Cliente).filter_by(idcliente=id_cliente).first()
        if cliente:
            for key, value in kwargs.items():
                setattr(cliente, key, value)
            session.commit()
            print("Cliente actualizado")
        else:
            print("Cliente no encontrado")

    @staticmethod
    def eliminar_cliente(session, id_cliente):
        cliente = session.query(Cliente).filter_by(idcliente=id_cliente).first()
        if cliente:
            session.delete(cliente)
            session.commit()
            print("Cliente eliminado correctamente")
        else:
            print("Cliente no encontrado")

