import os

# clase que permite realizar copias de seguridad
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
        # Comprobación de carpetas de origen y destino
        if not self.source_folder or not self.destination_folder:
            print("Por favor seleccione primero la carpeta de origen y la carpeta de destino.")
            return

        # Limpiar la pantalla
        os.system("cls")

        # Realizar la copia de seguridad
        info_backup = os.popen(f"robocopy {self.source_folder} {self.destination_folder}").read()
        print("Copia de seguridad completada con éxito.")
        input("Presione Enter para continuar...")

        # Verificar si existe el directorio de logs, si no, crearlo
        if not os.path.exists('logs'):
            os.mkdir('logs')

        # Obtener el contenido de logs existentes
        contenido_logs = os.listdir('logs')
        
        # Filtrar los archivos de log existentes
        existing_logs = [log for log in contenido_logs if log.startswith('log') and log.endswith('.txt')]

        # Verificar el número más alto entre los logs existentes
        if existing_logs:
            # Extraer números de los nombres de archivo de logs existentes
            existing_logs_numbers = [int(log.split('log')[1].split('.txt')[0]) for log in existing_logs]
            # Obtener el siguiente número para el nuevo log
            next_log_number = max(existing_logs_numbers) + 1
        else:
            # Si no hay logs existentes, crear el primero
            next_log_number = 1

        # Nombre del próximo archivo de log
        next_log_filename = f"log{next_log_number}.txt"

        # Escribir la información de la copia de seguridad en el nuevo archivo de log
        with open(f"logs/{next_log_filename}", "w") as file:
            file.write(info_backup)

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
