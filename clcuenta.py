"""
DAVID JULIAN CRIOLLO GOMEZ
VANESSA GUSTIN RODRIGUEZ
JUAN CAMILO INSUASTY GOMEZ
"""

from clusuario import usuario
class cuenta(usuario):

    def __init__(self, nombre, apellido, cedula, edad,dineroAhorrado):
        super().__init__(nombre, apellido, cedula, edad)
        self.__dineroAhorrado = dineroAhorrado

    def get_Dinero(self):
        return self.__dineroAhorrado

    def set_Dinero(self, dineroAh):
        self.__dineroAhorrado = dineroAh

    def mostrar(self):
        return print("Nombre: "+ self.get_Nombre() + "\n" + "Apellido: "+ self.get_Apellido() + "\n" "Cedula: "+ self.get_Cedula() + "\n" "Edad: "+ self.get_Edad() + "\n" "Saldo Disponible: $"+ str(self.get_Dinero()) + "\n")

    def ingresar(self, consignacion):
        if(consignacion>0):
            saldo = self.get_Dinero() + consignacion
            self.set_Dinero(saldo)
            return print("Su nuevo saldo es: $" + str(self.get_Dinero()), "\n")
        else: return print("La consignación no es valida \n")

    def retirar (self, cantidad):
        if(cantidad < self.get_Dinero()):
            saldo = self.get_Dinero()-cantidad
            self.set_Dinero(saldo)
            return print("Retiro existoso, su nuevo saldo disponible es: $" + str(self.get_Dinero()) + "\n")
        else: return print("No se puede hacer el retiro, la cantidad ingresada es superior al saldo disponible\n")



