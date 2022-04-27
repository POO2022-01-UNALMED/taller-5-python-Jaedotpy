from zooAnimales.animal import Animal
class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super.__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)

    # GET & SET #

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
    
    def getlargoCola(self):
        return self._largoCola
    
    def setlargoCola(self, largoCola):
        self._largoCola = largoCola

    # METODOS #
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        newIguana = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        cls.iguanas += 1
        return newIguana

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        newSnake = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        cls.serpientes += 1
        return newSnake
    
    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado) 