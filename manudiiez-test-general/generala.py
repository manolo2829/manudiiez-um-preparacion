from random import randint


class Dados:
    def __init__(self, cantidad_dados):
        self._valores = [randint(1, 6) for _ in range(cantidad_dados)]

    @property
    def cantidad(self):
        return len(self._valores)

    @property
    def valores(self):
        return self._valores


class Turno:
    def __init__(self):
        self.numero_lanzamiento = 1
        self.dados_lanzados = Dados(5)
        self.dados_seguir = Dados(0)

    @property
    def dados_finales(self):
        return self.dados_lanzados.valores + self.dados_seguir.valores

    def siguiente_turno(self):
        if(self.numero_lanzamiento >= 3):
            raise TurnoError("Limite de lanzamientos alcanzado")
        self.numero_lanzamiento += 1
        self.dados_lanzados = Dados(5 - self.dados_seguir.cantidad)
        
    def guardar_dados(self, indices):
        dados_finales_ant = self.dados_finales
        self.dados_seguir = Dados(0)
        for indice in indices:
            self.dados_seguir.valores.append(dados_finales_ant[indice])
        self.siguiente_turno()





class TurnoError(Exception):
    pass

class TablaPuntosError:
    def __init__(self):
        self.numero_lanzamiento = 1


class calcular_repetidos:
    def __init__(self):
        self.numero_lanzamiento = 1

class calcular_puntos:
    def __init__(self):
        self.numero_lanzamiento = 1

class TablaPuntos:
    def __init__(self):
        self.numero_lanzamiento = 1
