# metodos

from herenca_Encomenda_PAC import Encomenda_Pac
from heranca_Encomenda_Sedex import Encomenda_Sedex
from heranca_Encomenda_SedexPlus import Encomenda_SedexPlus

class Metodos:
    def __init__(self):
        self._encomendas = []
        self._total_receita = 0
        self._pac = []
        self._pac_receita = 0
        self._sedex = []
        self._sedex_receita = 0
        self._sedexplus = []
        self._sedexplus_receita = 0

    def verifica_op(self, op):
        if (op == 2 or op == 5 or op == 6) and len(self._encomendas) == 0:
            print('*Operação Inválida*\nNenhuma encomenda cadastrada')
            return False
    
        elif op != 1 and op != 2 and op != 3 and op != 4 and op != 5 and op != 6 and op != 7 and op != 8:
            print('*Operação Inexistente*')
            return False
    
        else:
            return True

    def verifica_tamanho(self, num_tipo, peso, altura, largura, comprimento):
        verifica = True

        if num_tipo == 3:
            if peso > 10:
                print('*Peso fora do limite (10 kg)*')
                verifica = False
        else:
            if peso > 30:
                print('*Peso fora do limite (30 kg)*')
                verifica = False
        if altura > 100:
            print('*Altura fora do limite (100 cm)*')
            verifica = False

        if largura > 100:
            print('*Largura fora do limite (100 cm)*')
            verifica = False

        if comprimento > 100:
            print('*Comprimento fora do limite (100 cm)*')
            verifica = False

        if comprimento + largura + altura > 200:
            print('*Soma do comprimento + largura + altura fora do limite (200 cm)*')
            verifica = False

        if peso <= 0 or altura <= 0 or largura <= 0 or comprimento <= 0:
            print('*Dimensões inexistentes.*')
            verifica = False

        if not verifica:
            print('Digite novamente as dimensões da encomenda')
        return verifica


    def busca_por_nome(self, nome_remetente):
        encomendas_remetente = []
        for encomenda in self._encomendas:
            if encomenda.nome_remetente == nome_remetente:
                encomendas_remetente.append(encomenda)
        
        return encomendas_remetente
    
    def busca_por_numero(self, num_encomenda):
        for encomenda in self._encomendas:
            if encomenda.num_encomenda == num_encomenda:
                return encomenda
        
        return None

    def adicionar_pac(self, nome_remetente, nome_destinatario, destino, peso, altura, largura, comprimento, fragilidade):
        num_encomenda = len(self._encomendas) + 1
        encomenda = Encomenda_Pac(num_encomenda, nome_remetente, nome_destinatario, destino, peso, altura, largura, comprimento, fragilidade)
        self._encomendas.append(encomenda)
        self._pac.append(encomenda)
        self._total_receita += encomenda.calculo_frete()
        self._pac_receita += encomenda.calculo_frete()

        return num_encomenda   

    def adicionar_sedex(self, nome_remetente, nome_destinatario, destino, peso, altura, largura, comprimento, fragilidade):
        num_encomenda = len(self._encomendas) + 1
        encomenda = Encomenda_Sedex(num_encomenda, nome_remetente, nome_destinatario, destino, peso, altura, largura, comprimento, fragilidade)
        self._encomendas.append(encomenda)
        self._sedex.append(encomenda)
        self._total_receita += encomenda.calculo_frete()
        self._sedex_receita += encomenda.calculo_frete()

        return num_encomenda
       
    def adicionar_sedexplus(self, nome_remetente, nome_destinatario, destino, peso, altura, largura, comprimento, fragilidade):
        num_encomenda = len(self._encomendas) + 1
        encomenda = Encomenda_SedexPlus(num_encomenda, nome_remetente, nome_destinatario, destino, peso, altura, largura, comprimento, fragilidade)
        self._encomendas.append(encomenda)
        self._sedexplus.append(encomenda)
        self._total_receita += encomenda.calculo_frete()
        self._sedexplus_receita += encomenda.calculo_frete()

        return num_encomenda
    
    def imprimir_encomenda(self, encomenda):
        print(f'Número de envio: {encomenda.num_encomenda}')
        print(f'Nome remetente: {encomenda.nome_remetente}')
        print(f'Nome destinatário: {encomenda.nome_destinatario}')
        print(f'Destino: {encomenda.destino}')
        print(f'Peso: {encomenda.peso} kg')
        print(f'Altura: {encomenda.altura} cm')
        print(f'Largura: {encomenda.largura} cm')
        print(f'Comprimento: {encomenda.comprimento} cm')
        print(f'Tipo envio: {encomenda.tipo}')
        print(f'Fragilidade: {encomenda.fragilidade}')
        print(f'Tempo de envio: {encomenda.prazo()} dia(s)')
        print(f'Preço frete: R$ {encomenda.calculo_frete():.2f}')

    def imprimir_encomendas(self, encomendas):
        for i, encomenda in enumerate(encomendas):
            print(f'Encomenda {i + 1}:')
            self.imprimir_encomenda(encomenda)
            print()

    def quant_encomendas(self):
        return len(self._encomendas)
    
    def quant_pac(self):
        return len(self._pac)
    
    def quant_sedex(self):
        return len(self._sedex)
    
    def quant_sedexplus(self):
        return len(self._sedexplus)

    def total_receita(self):
        return self._total_receita
    
    def receita_pac(self):
        return self._pac_receita
    
    def receita_sedex(self):
        return self._sedex_receita
    
    def receita_sedexplus(self):
        return self._sedexplus_receita
    
    def _calc_proporcao(self, total, parcial):
        return (parcial / total) * 100

    def proporcao_quant_pac(self):
        return self._calc_proporcao(len(self._encomendas), len(self._pac))

    def proporcao_quant_sedex(self):
        return self._calc_proporcao(len(self._encomendas), len(self._sedex))
    
    def proporcao_quant_sedexplus(self):
        return self._calc_proporcao(len(self._encomendas), len(self._sedexplus))
    
    def proporcao_receita_pac(self):
        return self._calc_proporcao(self._total_receita, self._pac_receita)
    
    def proporcao_receita_sedex(self):
        return self._calc_proporcao(self._total_receita, self._sedex_receita)
    
    def proporcao_receita_sedexplus(self):
        return self._calc_proporcao(self._total_receita, self._sedexplus_receita)

    def imprimir_historico_dia(self):
        print()
        print('Histórico do Dia')
        print()
        print('Encomendas')
        print(f'- Total: {self.quant_encomendas()} encomenda(s)')
        print(f'- PAC: {len(self._pac)} encomenda(s)')
        print(f'- Sedex: {len(self._sedex)} encomenda(s)')
        print(f'- SedexPlus: {len(self._sedexplus)} encomenda(s)')
        print()
        print('Receita')
        print(f'- Total: R$ {self._total_receita:.2f}')
        print(f'- PAC: R$ {self._pac_receita:.2f}')
        print(f'- Sedex: R$ {self._sedex_receita:.2f} ')
        print(f'- SedexPlus: R$ {self._sedexplus_receita:.2f} ')
        print()
        print('Dia Encerrado.')
        print()

    def finalizar_dia(self):
        self._encomendas.clear()
        self._total_receita = 0
        self._pac.clear()
        self._pac_receita = 0
        self._sedex.clear()
        self._sedex_receita = 0
        self._sedexplus.clear()
        self._sedexplus_receita = 0
        self._quant_encomendas = 0
