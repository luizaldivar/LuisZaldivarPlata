class Estadistica:
    def __init__(self, numeros):
        self.numeros = numeros
    
    # Estos métodos deben estar alineados con el def __init__
    def calcular_media(self):
        suma = sum(self.numeros)
        cantidad = len(self.numeros)
        return suma / cantidad
        
    def calcular_mediana(self):
        numeros_ordenados = sorted(self.numeros)
        n = len(numeros_ordenados)
        mitad = n // 2

        if n % 2 == 0:
            return (numeros_ordenados[mitad - 1] + numeros_ordenados[mitad]) / 2
        else:
            return numeros_ordenados[mitad]
            
    def calcular_moda(self):
        frecuencias = {}
        for numero in self.numeros:
            if numero in frecuencias:
                frecuencias[numero] += 1
            else:
                frecuencias[numero] = 1
        
        max_frecuencia = max(frecuencias.values())
        modas = []

        for numero, frecuencia in frecuencias.items():
            if frecuencia == max_frecuencia:
                modas.append(numero)

        if len(modas) == len(self.numeros):
            return "No hay moda"
        return modas
        
 