import datetime

class Fecha:
    def __init__(self, año=datetime.date.today().year, mes=datetime.date.today().month, dia=datetime.date.today().day):
        self.año = año
        self.mes = mes
        self.dia = dia

    def __repr__(self):
        return f"{self.dia}/{self.mes}/{self.año}"
    
    def compare_to(self, date):
        fecha = datetime.date(self.año, self.mes, self.dia)
        fecha2 = datetime.date(date.año, date.mes, date.dia)
        if(fecha < fecha2):
            return -1
        else:
            return 1 if fecha > fecha2 else 0