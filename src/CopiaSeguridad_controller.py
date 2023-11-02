import os
from src.clases.Backup import Backup

# Funcion que muestra el menu de copias de seguridad
def menu_copias():
    backup = Backup()
    backup.load_config()

    while True:
        os.system("cls")
        titulo()
        print("Seleccione una opción:")
        print("1. Seleccionar carpeta de origen")
        print("2. Seleccionar carpeta de destino")
        print("3. Ejecutar copia de seguridad")
        print("4. Programar copia de seguridad")
        print("5. Salir")

        option = input("Ingrese el número de opción: ")

        if option == "1":
            backup.select_source_folder()
        elif option == "2":
            backup.select_destination_folder()
        elif option == "3":
            backup.execute_backup()
        elif option == "4":
            pass
        elif option == "5":
            break
        else:
            print("Opción no válida. Por favor intente de nuevo.")

# Funcion que un tiulo del menu de copias de seguridad
def titulo():
    print("*********************************************")
    print("*                                           *")
    print("*        COPIAS DE SEGURIDAD                *")
    print("*                                           *")
    print("*********************************************")