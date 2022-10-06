# Váriveis
# int : int
# float : float
# string : str
# bool : bool
# print('1' + ' -' * 10 + ' 2')

# string_inteira = 'Parte1 Parte2'
# split = string_inteira.split(' ')
# print(split[0])
# print(split[1])

# Soma de 2 variáveis
cont = 1
while cont == 1:
    try:
        x = int(input('Digite o primeiro numero: '))
        y = int(input('Digite o segundo numero: '))
        x += y
        print()
        print(f'Resultado: {x}')
        cont = 0
    except:
        print('Por favor digite um numero')
        print()
