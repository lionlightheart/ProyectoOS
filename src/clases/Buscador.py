import os

class Buscador:
    def __init__(self):
        self.ruta_actual = os.getcwd()

    def mostar_directorio(self):
        return self.ruta_actual

    def cambiar_directorio(self, ruta:str):

        self.ruta_actual = ruta

print(os.getcwd())
print(os.listdir())
os.chdir("C:/Users/chivo/OneDrive/Documentos/ProyectoOS/src")
print(os.getcwd())
print(os.listdir())
os.system('ls')