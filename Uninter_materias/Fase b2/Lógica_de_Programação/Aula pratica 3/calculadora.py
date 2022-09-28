n1 = float(input('Digite o primeiro numero: '))
op = input('Digite a operação: ')
n2 = float(input('Digite o segundo numero: '))

if op == '+':
    n1 += n2
    print(f'Resultado: {n1}')

elif op == '-':
    n1 -= n2
    print(f'Resultado: {n1}')

elif op == '/':
    n1 /= n2
    print(f'Resultado: {n1}')

elif op == '*':
    n1 *= n2
    print(f'Resultado: {n1}')

else:
    print('Digite uma operação válida')