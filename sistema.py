from metodos import Metodos

metodos = Metodos()

encomenda1 = metodos.adicionar_pac('Joao', 'Maria', 'Floripa', 10, 78, 15, 20, 'Baixo')
encomenda2 = metodos.adicionar_sedex('Joao', 'Eduardo', 'POA', 30, 100, 30, 28, 'Moderado')
encomenda3 = metodos.adicionar_sedexplus('Pedro', 'Julia', 'SP', 5, 15, 5, 20, 'Altíssimo')
encomenda4 = metodos.adicionar_pac('Isa', 'Paula', 'RJ', 10, 50, 78, 30, 'Baixo')
encomenda5 = metodos.adicionar_pac('Claudio', 'Joana', 'Goias', 24, 92, 46, 39, 'Baixo')
encomenda6 = metodos.adicionar_sedexplus('Elton', 'Leandra', 'Salvador', 10, 95, 30, 20, 'Baixo')
encomenda7 = metodos.adicionar_sedex('Ana', 'Isabela', 'Curitiba', 10, 70, 50, 80, 'Alto')

while True:
    print('--MENU CORREIO--')
    print()
    print('OPERAÇÕES POSSÍVEIS:')
    print()
    print('1 - Cadastrar encomenda')
    print('2 - Pesquisar encomenda')
    print('3 - Quantidade de encomendas já cadastradas')
    print('4 - Receita até o momento')
    print('5 - Analise proporção tipo de encomenda em relação ao total de encomendas no dia')
    print('6 - Analise proporção tipo de encomenda em relação ao total da receita no dia')
    print('7 - Encerrar dia')
    print('8 - Encerrar programa')
    print()

    verificacao = False
    while not verificacao:
        op = int(input('Operação: '))
        verificacao = metodos.verifica_op(op)

    if op == 1:
        print()
        print('Cadastro Encomenda')
        print()

        print('Informações Iniciais')
        nome_remetente = input('Nome remetente: ').title().strip()
        nome_destinatario = input('Nome destinatário: ').title().strip()
        destino = input('Destino: ').title().strip()
        print()

        print('Tipo de envio')
        print('1 - PAC')
        print('2 - Sedex')
        print('3 - SedexPlus')
        num_tipo = int(input('Opção: '))
        while num_tipo != 1 and num_tipo != 2 and num_tipo != 3:
            num_tipo = int(input('*Opção Inválida*\nOpção: '))
        print()    

        verificacao = False
        while not verificacao:
            print('Dimensões encomenda')
            peso = int(input('Peso (kg): '))
            altura = int(input('Altura (cm): '))
            largura = int(input('Largura (cm): '))
            comprimento = int(input('Comprimento (cm): '))
            print()
            verificacao = metodos.verifica_tamanho(num_tipo, peso, altura, largura, comprimento)

        print('Nível de fragilidade')
        print('1 - Baixo')
        print('2 - Moderado')
        print('3 - Alto')
        print('4 - Altíssimo')
        op_fragilidade = int(input('Opção: '))
        while op_fragilidade != 1 and op_fragilidade != 2 and op_fragilidade != 3 and op_fragilidade != 4:
            op_fragilidade = int(input('*Opção Inválida*\nOpção: '))
        print()    
        
        if op_fragilidade == 1:
            fragilidade = 'Baixo' 

        elif op_fragilidade == 2:
            fragilidade = 'Moderado'

        elif op_fragilidade == 3:
            fragilidade = 'Alto'

        else:
            op_fragilidade = 'Altíssimo'
        
        if num_tipo == 1:
            num_encomenda = metodos.adicionar_pac(nome_remetente, nome_destinatario, destino, peso, altura, largura, comprimento, fragilidade)

        elif num_tipo == 2:
            num_encomenda = metodos.adicionar_sedex(nome_remetente, nome_destinatario, destino, peso, altura, largura, comprimento, fragilidade)

        else:
            num_encomenda = metodos.adicionar_sedexplus(nome_remetente, nome_destinatario, destino, peso, altura, largura, comprimento, fragilidade)

        print('Encomenda cadastrada com sucesso!')
        print(f'Número de envio: {num_encomenda}.')

    elif op == 2:
            print()
            print('Pesquisa Encomenda')
            print()

            print('Pesquiar por: ')
            print('1 - Nome do remetente')
            print('2 - Número de envio')
            op = int(input('Opção: '))
            while op != 1 and op != 2:
                op = int(input('*Opção Inválida*\nOpção: '))
            
            if op == 1:
                print('Pesquisa por nome')
                nome = input('Nome remetente: ').strip().title()
                encomendas = metodos.busca_por_nome(nome)
                if len(encomendas) > 0:
                    metodos.imprimir_encomendas(encomendas)                
                else:
                    print('Encomenda não encontrada.')

            elif op == 2:
                print('Pesquisa por número do envio')
                num_encomenda = int(input('Número de envio: '))
                encomenda = metodos.busca_por_numero(num_encomenda)
                if encomenda != None:
                    metodos.imprimir_encomenda(encomenda)
                else:
                    print('Encomenda não encontrada.')
            print()
        
    elif op == 3:
        print()
        print('Quantidade de Encomendas')
        print()
        print(f'- {metodos.quant_encomendas()} encomendas')
        print()
        
    elif op == 4:
        print()
        print('Receita até o momento no dia')
        print()
        print(f"R$ {metodos.total_receita():.2f}")
        print()
        
    elif op == 5:
        print()
        print('Proporção Total de Envios / Tipo de Envio')
        print()
        print('Total')
        print(f'- {metodos.quant_encomendas()} encomenda(s)')
        print()
        print('PAC')
        print(f'- Número absoluto: {metodos.quant_pac()} encomenda(s)')
        print(f'- Porcentagem: {metodos.proporcao_quant_pac():.2f} %')
        print()
        print('Sedex')
        print(f'- Número absoluto: {metodos.quant_sedex()} encomenda(s)')
        print(f'- Porcentagem: {metodos.proporcao_quant_sedex():.2f} %')
        print()
        print('SedexPlus')
        print(f'- Número absoluto: {metodos.quant_sedexplus()} encomenda(s)')
        print(f'- Porcentagem: {metodos.proporcao_quant_sedexplus():.2f} %')
        print()
            
    elif op == 6:
        print()
        print('Proporção Receita Total / Receita por Tipo de Envio')
        print()
        print('Total')
        print(f'- R$ {metodos.total_receita():.2f}')
        print()
        print('PAC')
        print(f'- Números absolutos: R$ {metodos.receita_pac():.2f}')
        print(f'- Porcentagem: {metodos.proporcao_receita_pac():.2f} %')
        print()
        print('Sedex')
        print(f'Número absoluto: R$ {metodos.receita_sedex():.2f}')
        print(f'- Porcentagem: {metodos.proporcao_receita_sedex():.2f} %')
        print()
        print('SedexPlus')
        print(f'Número absoluto: R$ {metodos.receita_sedexplus():.2f}')
        print(f'- Porcentagem: {metodos.proporcao_receita_sedexplus():.2f} %')
        print()
            
    elif op == 7:
        metodos.imprimir_historico_dia()
        metodos.finalizar_dia()
        
    else:
        print()
        print('Programa Encerrado.')
        break
