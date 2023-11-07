import os
from src.clases.Buscador import Buscador
# Funcion que utilizamos para mostrar e interactuar con el explorador de archivos
def menu_listar():
    buscador = Buscador()

    while True:
        os.system("cls")
        titulo()
        print("Seleccione una opción:")
        print("1. Mostrar ubicación actual")
        print("2. Listar archivos/directorios")
        print("3. Cambiar ubicación actual")
        print("4. Salir")

        option = int(input("Ingrese el número de opción: "))

        match option:
            case 1: 
                print(buscador.mostar_directorio())
                input("Presione Enter para continuar...")

            case 2:
                print(buscador.listar())
                input("Presione Enter para continuar...")

            case 3:
                ruta = buscador.mostar_directorio()
                nueva_ruta = input(f'Introduzca la ruta hacia la que desea navegar, actualmente se encuentra en {ruta}: \n ')
                print(buscador.cambiar_directorio(nueva_ruta))
            case 4:
                break
            case other:
                print("Opción no válida. Por favor intente de nuevo.")




def titulo():
    print("*********************************************")
    print("*                                           *")
    print("*        EXPLORADOR DE ARCHIVOS             *")
    print("*                                           *")
    print("*********************************************")