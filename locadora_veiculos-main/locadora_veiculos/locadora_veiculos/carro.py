from veiculo import Veiculo

class carro(Veiculo):
    def __init__(self, modelo, placa, ano, disponivel, valor_diaria):
        super().__init__(modelo, placa, ano, disponivel, valor_diaria)
        
    def alugar(self, dias):
        if self.disponivel:
            valor = self.calcular_diaria(dias)
            
            self.disponivel = False
        else:    
            print("Não tá disponível")
            
    def devolver(self, dias):
        if not self.disponivel:
            valor = self.calcular_diaria(dias)
            print(f"Valor total {valor}")
            
            self.disponivel = True
        
            print("Produto devolvido")
        
        else:
            print("Não foi devolvido")
        
    def calcular_diaria(self, dias):
        return self.valor_diaria * dias