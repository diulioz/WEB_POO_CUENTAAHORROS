from clbeneficio import beneficio
from clcuenta import cuenta
from clusuario import usuario

while True:
        print("*******************************************************************************")
        print("*                            MENU CUENTA-AHORROS                              *")
        print("*******************************************************************************")
        print("1. Ingresar datos de forma manual")
        print("2. Mostrar ejemplos")
        print("3. Salir")
        print("*******************************************************************************")
        opcion = int(input("Digite una opcion: "))
        print("\n")

        if opcion == 1:
             nombre_Usuario=str(input("Ingrese nombre: "))
             apellido_Usuario=str(input("Ingrese apellido: "))
             cedula_Usuario=str(input("Ingrese cedula: "))
             edad_Usuario=str(input("Ingrese edad: "))
             dinero_Ahorrado=float(input("Ingrese cantidad de dinero ahorrado: "))
             dinero_Retiro=float(input("Valor a retirar: "))

             cuenta0=beneficio(nombre_Usuario,apellido_Usuario,cedula_Usuario,edad_Usuario,dineroAhorrado=dinero_Ahorrado)
             cuenta0.ingresar(dinero_Ahorrado)
             cuenta0.mostrar()
             cuenta0.retirar(dinero_Retiro)
             cuenta0.mostrar()

        if opcion == 2:
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
        if opcion == 3:
            break