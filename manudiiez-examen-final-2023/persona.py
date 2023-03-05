from fecha import Fecha

class Persona:
    def __init__(self, id, apellido, nacimiento: Fecha()):
        self.id = id
        self.apellido = apellido
        self.nacimiento = nacimiento
    def _repr__(self):
        return f'{self.id} -- {self.apellido} -- {self.nacimiento}'
    
    # def compare_to(self, apellido):
    #     if self.apellido < apellido:
    #         return -1
    #     elif self.apellido == apellido:
    #         return 0
    #     elif self.apellido > apellido:
    #         return 1