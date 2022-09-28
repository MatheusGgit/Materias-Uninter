# Matheus Garcia de Oliveira
print('Bem-vindo ao Programa de feijoada do Matheus Garcia de Oliveira')

# Variáveis
cont = True
contFeijoada = True
cont_acompanhamento = True
cont_acompanhamento_feijoada = True
soma = 0

# Funções
def volumeFeijoada():
    while cont == True:
        try:
            volume = float(input('Insira o volume(ml): '))
            if volume < 300:
                print('Por favor, selecione um valor acima de 300 e abaixo de 5000')
                continue
            elif volume > 5000:
                print('Por favor, selecione um valor acima de 300 e abaixo de 5000')
                continue
            else:
                volume *= 0.08
                return volume
        except:
            print('Opção inválida!\n')
            continue

def opcaoFeijoada():
    while contFeijoada == True:
        try:
            escolha = int(input('>>> '))
            print()
            if escolha not in (1, 2 ,3):
                print('Opção inválida\n')
                continue
            else:
                if escolha == 1:
                    multiplicador = 1
                    return multiplicador
                elif escolha == 2:
                    multiplicador = 1.25
                    return multiplicador
                else:
                    multiplicador = 1.50
                    return multiplicador
        except:
            print('Opção inválida\n')
            continue

def acompanhamentoFeijoada():
    while cont_acompanhamento_feijoada == True:
        try:
            escolhaAcompanhamento = int(input('>>> '))
            print()

            if escolhaAcompanhamento not in (1, 2, 3, 4, 5):
                print('Opção inválida!\n')
            else:
                if escolhaAcompanhamento == 1:
                    valor = 5
                    return valor
                elif escolhaAcompanhamento == 2:
                    valor = 6
                    return valor
                elif escolhaAcompanhamento == 3:
                    valor = 7
                    return valor
                elif escolhaAcompanhamento == 4:
                    valor = 3
                    return valor
                else:
                    break
        except:
            print('Opção inválida\n')
            continue

# Inicio da função main
volume = volumeFeijoada()
print(f'R$ {volume}')

print('\nSelecione uma opção de feijoada: ')
print('1 - Básica(Feijão + paiol + costelinha)')
print('2 - Premium(Feijão + paiol + costelinha + partes do porco)')
print('3 - Suprema(Feijão + paiol+ costelinha + partes do porco + charque + calabresa + bacon)')
multiplicador = opcaoFeijoada()

print('Selecione um acompanhamento: ')
print('1 - 200g de arroz (R$ 5,00)')
print('2 - 150g de farofa especial (R$ 6,00)')
print('3 - 100g de couve cozida (R$ 7,00)')
print('4 - 1 laranja descascada (R$ 3,00)')
print('5 - Não quero acompanhamento(encerrar pedido)')
valor = acompanhamentoFeijoada()

while cont_acompanhamento == True:
    print('Deseja pedir mais um acompanhamento? [S/N]')
    escolha_cont = input('>>> ')
    print()

    if escolha_cont.lower() not in 'sn':
        print('Opção inválida\n')
        continue
    else:
        if escolha_cont.lower() == 'n':
            break
        else:
            atual = valor
            valor = acompanhamentoFeijoada()
            valor += atual

soma = (volume * multiplicador) + valor
print(f'Total a ser pago: {soma}')