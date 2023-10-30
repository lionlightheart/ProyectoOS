import os

class Backup:
    def __init__(self):
        self.source_folder = None
        self.destination_folder = None
        self.file_path = "backup_config.txt"

    def select_source_folder(self):
        os.system("cls")
        try:
            self.source_folder = input("Ingrese la ruta de la carpeta a copiar: ")
            self.save_config()
        except:
            print("La ruta ingresada no es válida.")

    def select_destination_folder(self):
        os.system("cls")
        self.destination_folder = input("Ingrese la ruta de la carpeta de destino: ")
        self.save_config()

    def execute_backup(self):
        if not self.source_folder or not self.destination_folder:
            print("Por favor seleccione primero la carpeta de origen y la carpeta de destino.")
            return
        os.system("cls")
        os.system(f"robocopy {self.source_folder} {self.destination_folder}")
        print("Copia de seguridad completada con éxito.")
        input("Presione Enter para continuar...")

    def save_config(self):
        with open(self.file_path, "w",encoding="utf-8") as f:
            f.write(f"source_folder={self.source_folder}\n")
            f.write(f"destination_folder={self.destination_folder}\n")

    def load_config(self):
        if not os.path.exists(self.file_path):
            return

        with open(self.file_path, "r",encoding="utf-8") as f:
            for line in f:
                key, value = line.strip().split("=")
                if key == "source_folder":
                    self.source_folder = value
                elif key == "destination_folder":
                    self.destination_folder = value
