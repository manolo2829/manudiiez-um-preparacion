from base import Base
from fecha import Fecha
from persona import Persona
from service import Service

if __name__ == '__main__':
    fecha1 = Fecha(2022, 3, 14)
    fecha2 = Fecha(2024, 6, 1)
    fecha3 = Fecha() # hoy
    fecha4 = Fecha(1995, 11, 11)
    persona1 = Persona(5, 'Perez', fecha1)
    persona2 = Persona(2, 'Gomez', fecha2)
    persona3 = Persona(1, 'Diaz', fecha3)
    persona4 = Persona(4, 'Zen', fecha4)

    base = Base()
    service = Service()
    service.add(persona1, base)
    service.add(persona2, base)
    service.add(persona3, base)
    service.add(persona4, base)
    resultado = service.order_by_fecha(base)
