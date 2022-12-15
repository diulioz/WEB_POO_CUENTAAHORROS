from clbeneficio import beneficio
from clcuenta import cuenta
import sys
class Banco:

    def __init__(self) -> None:
        self.menu()
        
    def ingresar_datos(self):
        nombre_Usuario=str(input("Ingrese nombre: "))
        if nombre_Usuario.isalpha():
            pass
        else: 
            print("Por favor ingrese un valor alfabetico")
            self.menu()
        apellido_Usuario=str(input("Ingrese apellido: "))
        if nombre_Usuario.isalpha():
            pass
        else: 
            print("Por favor ingrese un valor alfabetico")
            self.menu()
        try:
            cedula_Usuario=int(input("Ingrese cedula: "))
        except ValueError:
            print("Por favor ingrese un valor numerico")
            self.menu()
        try:
            edad_Usuario=int(input("Ingrese edad: "))
        except ValueError:
            print("Por favor ingrese un valor numerico")
            self.menu()
        try:
            dinero_Ahorrado=float(input("Ingrese cantidad de dinero ahorrado: "))
        except ValueError:
            print("Por favor ingrese un valor numerico")
            self.menu()

        self.bn = beneficio(nombre_Usuario, apellido_Usuario, cedula_Usuario, edad_Usuario, dinero_Ahorrado)

        return self.bn

    def menu(self):
        while True:
            print("*******************************************************************************")
            print("*                            MENU CUENTA-AHORROS                              *")
            print("*******************************************************************************")
            print("1. Agregar usuario")
            print("2. Retirar")
            print("3. Consignar")
            print("4. Mostrar Datos")
            print("5. Mostrar ejemplos")
            print("6. Salir")
            print("*******************************************************************************")
            
            opcion = int(input("Digite una opcion: "))
            print("\n")
            if opcion == 1:
                self.usuario = self.ingresar_datos()
                self.usuario.edadUsuario()
                
            elif opcion == 2:
                cantidad = int(input("Ingrese el valor a retirar: "))
                if cantidad < 0:
                    print("Por favor ingrese valores positivos")
                else:
                    self.usuario.retirar(cantidad)

            elif opcion == 3:
                cantidad = int(input("Ingrese el valor a consignar: "))
                if cantidad < 0:
                    print("Por favor ingrese valores positivos")
                else:
                    self.usuario.ingresar(cantidad)
                    self.usuario.edadUsuario()

            elif opcion == 4:
                self.usuario.mostrar()

            elif opcion == 5:
                cuenta1=cuenta("david", "julian", "1234", "23", 15000)
                cuenta1.mostrar()
                cuenta1.ingresar(500)
                cuenta1.mostrar()
                cuenta1.retirar(20000)
                cuenta1.mostrar()
                cuenta1.retirar(1500)
                cuenta1.mostrar()

                cuenta2=beneficio("Vanessa", "Gustin", "78589524", "17", 100000)
                cuenta2.edadUsuario() 
                cuenta2.mostrar()
                cuenta3=beneficio("Dana", "Criollo", "54725645", "23", 100000)
                cuenta3.edadUsuario() 
                cuenta3.mostrar()
                cuenta4=beneficio("Juan", "Insuasty", "28754852", "32", 100000)
                cuenta4.edadUsuario() 
                cuenta4.mostrar()
            elif opcion == 6:
                break
            else:
                print("Por favor ingrese una opción válida")

Banco()