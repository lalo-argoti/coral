from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.core.Mirlt import Base

class Alumno(Base):
    __tablename__ = 'occb_alumnos'

    id_alumno = Column(Integer, primary_key=True, autoincrement=True)
    identidad = Column(String(16), nullable=False, unique=True)
    c_exp_id = Column(String(16), nullable=True)
    f_exp_id = Column(Date, nullable=True)
    apellidos = Column(String(32), nullable=False)
    nombres = Column(String(32), nullable=False)
    genero = Column(String(1), nullable=True)
    acudiente = Column(Integer, ForeignKey('occb_acudientes.id_acudiente'), nullable=False)
    madre = Column(Integer, nullable=True)
    padre = Column(Integer, nullable=True)
    f_nacimiento = Column(Date, nullable=True)
    sangre = Column(String(8), nullable=True)
    eps = Column(String(16), nullable=True)
    estrato = Column(Integer, nullable=True)
    email = Column(String(64), nullable=True)

    acudiente_info = relationship("Acudiente", back_populates="alumnos")

class Acudiente(Base):
    __tablename__ = 'occb_acudientes'

    id_acudiente = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(64), nullable=False)
    telefono = Column(String(16), nullable=True)
    cedula = Column(String(16), nullable=False, unique=True)
    direccion = Column(String(128), nullable=True)
    email = Column(String(64), nullable=True)

    alumnos = relationship("Alumno", back_populates="acudiente_info")

