class GLC():
    def __init__(self,nombre,no_terminales,terminales,inicial,transiciones):
        self.nombre=nombre
        self.no_terminales=no_terminales
        self.terminales=terminales
        self.inicial= inicial
        self.transiciones=transiciones

class GRAMA():
    def __init__(self,no_terminales,transiciones):
        self.no_terminales=no_terminales
        self.transiciones=transiciones

