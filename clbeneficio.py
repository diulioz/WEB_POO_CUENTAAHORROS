"""
DAVID JULIAN CRIOLLO GOMEZ
VANESSA GUSTIN RODRIGUEZ
JUAN CAMILO INSUASTY GOMEZ
"""

from clcuenta import cuenta

class beneficio(cuenta):
    def __init__(self, nombre, apellido, cedula, edad, dineroAhorrado):
        super().__init__(nombre, apellido, cedula, edad, dineroAhorrado)

    def calcularInteres(self):
        calculo = self.get_Dinero()*0.05
        calculo = self.get_Dinero() + calculo
        self.set_Dinero(calculo)

    def edadUsuario(self):
        if(int(self.get_Edad())>17 and int(self.get_Edad())<28):
            self.calcularInteres()
            return True
        else: return False

    def mostrar(self):
        return print("Nombre: "+ str(self.get_Nombre()) + "\n" + "Apellido: "+ str(self.get_Apellido()) + "\n" "Cedula: "+ str(self.get_Cedula()) + "\n" "Edad: "+ str(self.get_Edad()) + "\n" "Saldo Disponible: $"+ str(self.get_Dinero()) + "\n") 


