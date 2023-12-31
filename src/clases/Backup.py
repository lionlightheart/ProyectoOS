""" Esta parte de la práctica fue nuestra primera idea y la que íbamos a desarrollar, por lo que trabajamos un poco en ella todos al principio,
César hizo una aplicación sencilla que copiaba el contenido de una carpeta en otra, Rámon la pasó orientada a objetos y Franco hizo la parte
de mantener la configuracion del usuario para posteriores copias. Posteriormente César añadio que esas copias fuesen comprimidas y se crease
una carpeta logs con los registros de las copias de seguridad. """

import os

# clase que permite realizar copias de seguridad
class Backup:
    def __init__(self):
        self.source_folder = None
        self.destination_folder = None
        self.file_path = "backup_config.txt"

    def select_source_folder(self, ruta_carpeta):
        try:
            self.source_folder = ruta_carpeta 
            self.save_config()
        except:
            return False

    def select_destination_folder(self, ruta_destino):
        self.destination_folder = ruta_destino
        self.save_config()

    def execute_backup(self):
        # Comprobación de carpetas de origen y destino
        if not self.source_folder or not self.destination_folder:
            print("Por favor seleccione primero la carpeta de origen y la carpeta de destino.")
            return

        os.system("cls")

        # Comprimir la carpeta de origen
        os.system(f'powershell Compress-Archive -Path {self.source_folder} -DestinationPath {os.path.join(self.source_folder, "temp.zip")}')

        # Creo una carpeta temp para guardar ahí la posterior compresion del directorio porque para hacerlo con robocopy no podia hacerlo directamente
        if not os.path.exists(self.source_folder+"/temp"):
            os.mkdir(self.source_folder+"/temp")
        
        # Elegir el primer nombre disponible
        files_in_destination = [file for file in os.listdir(self.destination_folder) if file.endswith('.zip')]
        next_number = len(files_in_destination) + 1
        new_backup_filename = f'Copia de seguridad de {os.path.basename(self.source_folder)}_[{next_number}].zip'

        os.rename(os.path.join(self.source_folder, 'temp.zip'), os.path.join(self.source_folder+'/temp', new_backup_filename))
        
        # Realizar la copia de seguridad con Robocopy, incluyendo el archivo .zip
        info_backup = os.popen(f"robocopy {self.source_folder+'/temp'} {self.destination_folder}").read()        

        # Eliminar la carpeta 'temp' junto con su contenido
        temp_folder = os.path.join(self.source_folder, "temp")
        for root, dirs, files in os.walk(temp_folder, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                os.rmdir(dir_path)
        os.rmdir(temp_folder)
        
        print("Copia de seguridad completada con éxito.")
        
        # Verificar si existe el directorio de logs, si no, crearlo
        if not os.path.exists('logs'):
            os.mkdir('logs')

        # Obtener el contenido de logs existentes
        contenido_logs = os.listdir('logs')
        
        # Filtrar los archivos de log existentes
        existing_logs = [log for log in contenido_logs if log.startswith('log') and log.endswith('.txt')]

        # Verificar el número más alto entre los logs existentes
        if existing_logs:
            existing_logs_numbers = [int(log.split('log')[1].split('.txt')[0]) for log in existing_logs]
            next_log_number = max(existing_logs_numbers) + 1
        else:
            next_log_number = 1

        # Nombre del próximo archivo de log
        next_log_filename = f"log{next_log_number}.txt"

        # Escribir la información de la copia de seguridad en el nuevo archivo de log
        with open(f"logs/{next_log_filename}", "w") as file:
            file.write(info_backup)
                
        return info_backup
        
    # Guardamos la configuración en un fichero para que el usuario no tenga que configurar las carpetas siempre
    def save_config(self):
        with open(self.file_path, "w",encoding="utf-8") as f:
            f.write(f"source_folder={self.source_folder}\n")
            f.write(f"destination_folder={self.destination_folder}\n")

    # Cargamos la config
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
    