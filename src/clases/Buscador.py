from os import listdir, getcwd, path, chdir

# Clase que permite listar archivos y directorios, cambiar de directorio y mostrar la ruta actual
class Buscador:
    
    def __init__(self):
        self.ruta_actual = getcwd()

    def mostar_directorio(self):
        return self.ruta_actual

    def cambiar_directorio(self, nueva_ruta:str):
        if path.exists(nueva_ruta):
            self.ruta_actual = nueva_ruta
            return chdir(self.ruta_actual)
            
    def listar(self):
        return listdir()
    
        
    
    

