import os

# Clase que obtiene la informacion del pc
class PcInfo:
    def __init__(self):
        self.pc_os = self.get_os()
        self.pc_name = self.get_pc_name()
        self.pc_cpu = self.get_cpu()
        self.pc_gpu = self.get_gpu()
        self.pc_ram = self.get_ram()
        self.pc_hard_disk_count = self.get_count_disk()
    
    def __str__(self):
        return f"Sistema operativo: {self.pc_os}\nPC: {self.pc_name}\nCPU: {self.pc_cpu}\nGPU: {self.pc_gpu.strip()}\nRAM: {self.pc_ram}GB\nDISCOS: {self.pc_hard_disk_count}"
    
    def get_os(self):
        return "Windows" if os.name == "nt" else "Linux"
    
    def get_pc_name(self):
        return os.environ["COMPUTERNAME"] if os.name == 'nt' else os.uname()[1]
    
    def get_ram(self):
        resultado = os.popen("wmic ComputerSystem get TotalPhysicalMemory").read()
        lineas = resultado.strip().split("\n")
        memoria_total = round(int(lineas[2].strip()) / (1024**3), 1)
        return memoria_total
    
    def get_count_disk(self):
        resultado = os.popen("wmic diskdrive get DeviceID,Model,Size,MediaType /format:list").read()
        discos = []
        disco_actual = {}
        count = 0
        for linea in resultado.strip().split('\n'):
            if linea.strip():
                clave, valor = linea.split('=', 1)
                disco_actual[clave.strip()] = valor.strip()
            else:
                discos.append(disco_actual)
                disco_actual = {}
                
        for disco in discos:
            for disco_clave in disco:
                if disco_clave == "Model":
                    count += 1
        
        return count
    
    def get_cpu(self):
        resultado = os.popen("wmic cpu get Name /format:list").read()
        return resultado.strip().split("=")[1]
    
    def get_gpu(self):
        resultado = os.popen("wmic path win32_VideoController get name /format:list").read()
        return resultado.strip().split("=")[1].split("\n")[0].strip()
