"""
DAVID JULIAN CRIOLLO GOMEZ
VANESSA GUSTIN RODRIGUEZ
JUAN CAMILO INSUASTY GOMEZ
"""

from clusuario import usuario
class cuenta(usuario):
#     heredar los datos de usuario, y definir el atributo para la cantidad
# de dinero ahorrado. En esta clase, definir el constructor, 
# los métodos set y get para actualizar
# y obtener valores de los atributos, método mostrar 
# para indicar un resumen del cliente y el
# dinero que tiene en la cuenta, método ingresar para 
# simular una consignación de dinero
# (validar valores negativos) y método retirar para 
# disminuir una cantidad de dinero en la cuenta.
    def __init__(self, nombre, apellido, cedula, edad,dineroAhorrado):
        super().__init__(nombre, apellido, cedula, edad)
        self.__dineroAhorrado = dineroAhorrado

    def get_Dinero(self):
        return self.__dineroAhorrado

    def set_Dinero(self, dineroAh):
        self.__dineroAhorrado = dineroAh

    def mostrar(self):
        return "Nombre: "+ self.get_Nombre() + "\n" + "Apellido: "+ self.get_Apellido() + "\n" "Cedula: "+ self.get_Cedula() + "\n" "Edad: "+ self.get_Edad() + "\n" "Saldo Disponible: "+ str(self.get_Dinero()) + "\n" 


cuenta1=cuenta("david", "julian", "1234", "23", 15000)
print(cuenta1.get_Nombre())
print(cuenta1.get_Apellido())
print(cuenta1.get_Cedula())
print(cuenta1.get_Edad())
print(cuenta1.get_Dinero())
print(cuenta1.mostrar())

