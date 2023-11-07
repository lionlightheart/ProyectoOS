from os import listdir, getcwd, path, chdir

# Clase que permite listar archivos y directorios, cambiar de directorio y mostrar la ruta actual
class Buscador:
    
    def __init__(self): 
        self.ruta_actual = getcwd()

    def mostar_directorio(self):
        return self.ruta_actual

    # Comprobamos si existe la ruta y cambiamos
    def cambiar_directorio(self, nueva_ruta:str):
        if path.exists(nueva_ruta):
            self.ruta_actual = nueva_ruta
            chdir(self.ruta_actual)
            return self.ruta_actual
    
    # Listamos los directorios y ficheros que tiene la ruta        
    def listar(self): 
        return listdir()

    # Comprueba si un elemento es directorio o fichero
    def es_directorio(self,ruta):#Función que verifica si la ruta es un directorio.
        if path.isdir(ruta):
            return True
        else:
            return False
    
        
    
    

