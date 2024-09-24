from heranca_Encomenda import Encomenda

class Encomenda_SedexPlus(Encomenda):
    def __init__(self, num_encomenda, nome_remetente, nome_destinatario, destino, peso, altura, largura, comprimento, fragilidade):
        super().__init__(num_encomenda, nome_remetente, nome_destinatario, destino, peso, altura, largura, comprimento, 'SedexPlus', fragilidade)

    def calculo_frete(self):
        frete = ((self.altura * self.peso + self.largura * self.comprimento) / 1000) * 15 #cosntante para o tipo de Encomenda Sedex
        return frete
    
    def prazo(self):
        return 1
    