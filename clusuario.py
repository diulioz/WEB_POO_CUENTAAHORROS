"""
DAVID JULIAN CRIOLLO GOMEZ
VANESSA GUSTIN RODRIGUEZ
JUAN CAMILO INSUASTY GOMEZ
"""

class usuario:
    #nombre, apellido, cédula, edad) y método
#constructor.
    def __init__(self, nombre, apellido, cedula, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.edad = edad

    def get_Nombre(self):
        return self.nombre
    def get_Apellido(self):
        return self.apellido
    def get_Cedula(self):
        return self.cedula
    def get_Edad(self):
        return self.edad