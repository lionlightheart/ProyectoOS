from src.clases.PcInfo import PcInfo
from src.CopiaSeguridad_controller import menu_copias
import os

def main():
    pc = PcInfo()
    while True:
        os.system("cls")
        titulo_main()
        print("Seleccione una opción:")
        print("1. Copia de seguridad")
        print("2. Información de la PC")
        print("3. Salir")
        option = input("Ingrese el número de opción: ")
        if option == "1":
            os.system("cls")
            menu_copias()
        elif option == "2":
            os.system("cls")
            titulo_info()
            print(pc)
            input("Presione Enter tecla para continuar...")
        elif option == "3":
            break
        else:
            os.system("cls")
            print("Opción no válida. Por favor intente de nuevo.")

def titulo_main():
    print("*********************************************")
    print("*                                           *")
    print("*        EJEMPLO DE LIBRERÍA OS             *")
    print("*                                           *")
    print("*********************************************")

def titulo_info():
    print("*********************************************")
    print("*                                           *")
    print("*        INFORMACIÓN DEl PC                 *")
    print("*                                           *")
    print("*********************************************")    

if __name__ == "__main__":
    main()