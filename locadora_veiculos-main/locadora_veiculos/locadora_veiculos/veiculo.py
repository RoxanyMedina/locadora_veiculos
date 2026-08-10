from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, modelo, placa, ano, disponivel, valor_diaria):
       self.__modelo = modelo
       self.__placa = placa
       self.__ano = ano
       self.__disponivel = disponivel
       self.__valor_diaria = valor_diaria
    
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo
        
    
    @property
    def placa(self):
        return self.__placa
    
    @placa.setter
    def placa(self, placa):
        self.__placa = placa
        
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        self.__ano = ano

            
    @property
    def disponivel(self):
        return self.__disponivel
    
    @disponivel.setter
    def disponivel(self, disponivel):
        self.__disponivel = disponivel

    @property
    def valor_diaria(self):
        return self.__valor_diaria
    
    @valor_diaria.setter
    def valor_diaria(self, valor_diaria):
        self.__valor_diaria = valor_diaria
        
        
    @abstractmethod
    def alugar(self, dias):
        pass

    @abstractmethod
    def devolver(self, dias):
        pass
    
    @abstractmethod
    def calcular_diaria(self, dias):
        pass
            
        # if veiculo == 'moto' and dias > 7: 
        #     print("Tem 10% de desconto")
        #     return (valor*0,10)
    