from persona import Persona
from base import Base


class Service:
    def __init__(self):
        self.data = {}

    def add(self, persona: Persona, base: Base):
        base.data[persona.id] = persona


    def order_by_fecha(self, base: Base):
        auxiliar = []
        for i in base.data:
            element = base.data[i]
            if len(auxiliar) == 0:
                auxiliar.append(element)
            else:
                for num in range(len(auxiliar)):
                    result = element.nacimiento.compare_to(auxiliar[num].nacimiento)
                    if result == -1 or result == 0:
                        auxiliar.insert(num, element)
                        break
                    elif( num == len(auxiliar)-1):
                        auxiliar.append(element)
        return auxiliar
    
    
    
    def order_by_apellido(self, base: Base):
        auxiliar = []
        for i in base.data:
            element = base.data[i]
            if len(auxiliar) == 0:
                auxiliar.append(element)
            else:
                for num in range(len(auxiliar)):
                    result = element.compare_to(auxiliar[num].apellido)
                    if result == -1 or result == 0:
                        auxiliar.insert(num, element)
                        break
                    elif( num == len(auxiliar)-1):
                        auxiliar.append(element)
                    
        return auxiliar