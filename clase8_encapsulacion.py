class CasillaVotacion:
    def __init__(self, identificador, pais):
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError(f"La región {region} no es valida en {self.__pais}")

casilla = CasillaVotacion(123, ["Popayán"])
casilla.region
print(casilla.region)
casilla.region = "Popayán"
print(casilla.region)

#vimos como usamos la función que trae integrada python que es @property y el ejercicio es validar si la region está en el pais
#y al país lo colocamos dentro de un array o lista
