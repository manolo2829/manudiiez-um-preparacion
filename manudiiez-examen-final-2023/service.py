from base import Base
from persona import Persona

class Service:

    def add(self, persona: Persona=None, base: Base=None):
        base.data[persona.id] = persona
        
    def order_by_fecha(self, base: Base=None):
        orderDates = []
        
        for element in base.data.values():
            if len(orderDates) == 0:
                orderDates.append(element)
            else:
                for i in range(len(orderDates)):
                    if element.nacimiento.compare_to(orderDates[i].nacimiento) == -1 or element.nacimiento.compare_to(orderDates[i].nacimiento) == 0:
                        orderDates.insert(i, element)
                        break
                    elif i == len(orderDates)-1:
                        orderDates.append(element)
                        break
                    elif element.nacimiento.compare_to(orderDates[i].nacimiento) == 1:
                        pass
                        

        return orderDates
    
    def order_by_apellido(self, base: Base=None):
        orderApellidos = []
        
        for element in base.data.values():
            if len(orderApellidos) == 0:
                orderApellidos.append(element)
            else:
                for i in range(len(orderApellidos)):
                    if element.apellido < orderApellidos[i].apellido:
                        orderApellidos.insert(i, element)
                        break
                    elif i == len(orderApellidos)-1:
                        orderApellidos.append(element)
                        break
                    elif element.apellido > orderApellidos[i].apellido:
                        pass
                        

        return orderApellidos