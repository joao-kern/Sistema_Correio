class Encomenda:
    def __init__(self, num_encomenda, nome_remetente, nome_destinatario, destino, peso, altura, largura, comprimento, tipo, fragilidade):
        self.num_encomenda = num_encomenda
        self.nome_remetente = nome_remetente
        self.nome_destinatario = nome_destinatario
        self.destino = destino
        self.peso = peso
        self.altura = altura
        self.largura = largura
        self.comprimento = comprimento
        self.tipo = tipo
        self.fragilidade = fragilidade

    def volume(self):
        return self.altura * self.comprimento * self.largura
    
    def verifica_tamanho(self):
        pass

    def calculo_frete(self):
        pass

    def prazo(self):
        pass
    