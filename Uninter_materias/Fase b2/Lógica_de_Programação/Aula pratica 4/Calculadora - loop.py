continua = 1
while continua == 1:
    n1 = float(input('Digite o primeiro numero: '))
    if n1 == 0:
        break
    op = input('Digite a operação: ')
    if op == '0':
        break
    n2 = float(input('Digite o segundo numero: '))
    if n2 == 0:
        break

    if op == '+':
        n1 += n2
        print(f'Resultado: {n1}')
        print()

    elif op == '-':
        n1 -= n2
        print(f'Resultado: {n1}')
        print()

    elif op == '/':
        n1 /= n2
        print(f'Resultado: {n1}')
        print()

    elif op == '*':
        n1 *= n2
        print(f'Resultado: {n1}')
        print()

    else:
        print('Digite uma operação válida')
        print()

print('Calculadora encerrada!')
