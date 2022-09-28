# Matheus Garcia de Oliveira
print('Bem-vindo a Pizzaria do Matheus Garcia de Oliveira')

# Variáveis
cont = 's'
valor = 0.0
carrinho = 0

# Início
print('>>> Menu <<<')
print('Código | Descrição  |  Pizza Média | Pizza Grande')
print('21     | Napolitana |   R$: 20,00  |     R$ 26,00')
print('22     | Margherita |   R$: 20,00  |     R$ 26,00')
print('23     | Calabresa  |   R$: 25,00  |     R$ 32,50')
print('24     | Toscana    |   R$: 30,00  |     R$ 39,00')
print('25     | Portuguesa |   R$: 30,00  |     R$ 39,00')

while cont == 's':
    try:
        cod = int(input('Digite o código do produto: '))
        if cod not in (21, 22, 23, 24, 25):
            print('Código inválido\n')

        elif cod == 21:
            print('Pizza: Napolitana')
            valor = 20

        elif cod == 22:
            print('Pizza: Margherita')
            valor = 20

        elif cod == 23:
            print('Pizza: Calabresa')
            valor = 25

        elif cod == 24:
            print('Pizza: Toscana')
            valor = 30

        elif cod == 25:
            print('Pizza: Portuguesa')
            valor = 30

        # Continuará perguntando o tamanho da pizza até receber um valor válido
        j = 0
        while j < 1:
            print('Selecione o tamanho [M/G]')
            tamanho = input('>>> ')

            if tamanho.lower() not in 'mg':
                print('Opção inválida\n')
                continue
            else:
                if tamanho.lower() == 'g':
                    valor = ((30 * valor) / 100) + valor

                carrinho += valor
                break

        # Continuará perguntando se deseja pedir novamente até receber um valor válido
        i = 0
        while i < 1:
            print('\nDeseja pedir mais alguma coisa? [S/N]')
            escolha = input('>>> ')

            if escolha.lower() in 'sn':
                if escolha.lower() == 'n':
                    cont = 'n'
                break
            else:
                print('Opção inválida')
                continue
        print() # Para pular uma linha, apenas para organização

    except:
        print('Opção Inválida\n')

print('Finalizado!')
print(f'Valor total: R$ {round(carrinho, 3)}')