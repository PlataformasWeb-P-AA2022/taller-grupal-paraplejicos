from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import enlace

engine = create_engine(enlace)

from app import Docente

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objetos de tipo Docente
docente1 = Docente(n_propietario="Tony", placa="LBC-1878", \
        anio="2019", precio="150")

docente2 = Docente(n_propietario="Luis", placa="LBD-1254", \
        anio="2020", precio="210")

docente3 = Docente(n_propietario="Ana", placa="ABI-1345", \
        anio="2020", precio="230")

docente4 = Docente(n_propietario="Monica", placa="LBX-187", \
        anio="2003", precio="25")

# se agrega los objetos
# a la sesión
# a la espera de un commit
# para agregar un registro a la base de
# datos
session.add(docente1)
session.add(docente2)
session.add(docente3)
session.add(docente4)

# se confirma las transacciones
session.commit()
