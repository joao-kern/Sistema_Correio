from heranca_Encomenda import Encomenda

class Encomenda_Sedex(Encomenda):
    def __init__(self, num_encomenda, nome_remetente, nome_destinatario, destino, peso, altura, largura, comprimento, fragilidade):
        super().__init__(num_encomenda, nome_remetente, nome_destinatario, destino, peso, altura, largura, comprimento, 'Sedex', fragilidade)

    def calculo_frete(self):
        frete = ((self.altura * self.peso + self.largura * self.comprimento) / 1000) * 12 #cosntante para o tipo de Encomenda Sedex
        return frete
    
    def prazo(self):
        return 3
    
    
    