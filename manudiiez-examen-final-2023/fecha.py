import datetime


class Fecha:
    def __init__(self, año=datetime.date.today().year, mes=datetime.date.today().month, dia=datetime.date.today().day):
        self.año = año
        self.mes = mes
        self.dia = dia
    def __repr__(self):
        return f'{self.año}/{self.mes}/{self.dia}'
    
    def compare_to(self, date_to_compare):
        date = datetime.date(self.año, self.mes, self.dia)
        date_to_compare = datetime.date(date_to_compare.año, date_to_compare.mes, date_to_compare.dia)
        
        if(date == date_to_compare):
            return 0
        else:
            return 1 if date > date_to_compare else -1
        