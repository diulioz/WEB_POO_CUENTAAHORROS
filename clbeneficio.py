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
        return print("Nombre: "+ self.get_Nombre() + "\n" + "Apellido: "+ self.get_Apellido() + "\n" "Cedula: "+ self.get_Cedula() + "\n" "Edad: "+ self.get_Edad() + "\n" "Saldo Disponible: $"+ str(self.get_Dinero()) + "\n") 


cuenta1=beneficio("david", "julian", "1234", "23", 15000)
cuenta1.ingresar(500)
cuenta1.mostrar()
cuenta1.retirar(20000)
cuenta1.mostrar()
cuenta1.retirar(1500)
cuenta1.mostrar()

cuenta2=beneficio("david", "julian", "1234", "17", 100000)
cuenta2.edadUsuario() 
cuenta2.mostrar()
cuenta3=beneficio("david2", "julian2", "1234", "23", 100000)
cuenta3.edadUsuario() 
cuenta3.mostrar()
cuenta4=beneficio("david3", "julian3", "1234", "32", 100000)
cuenta4.edadUsuario() 
cuenta4.mostrar()