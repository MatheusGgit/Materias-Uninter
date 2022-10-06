valor = float(input('Digite o valor em reais: '))

if valor >= 100:
    cedulas100 = valor // 100
    valor -= cedulas100 * 100
    print(f'Cedulas de 100: {cedulas100}')

if valor >= 50:
    cedulas50 = valor // 50
    valor -= cedulas50 * 50
    print(f'Cedulas de 50: {cedulas50}')

if valor >= 20:
    cedulas20 = valor // 20
    valor -= cedulas20 * 20
    print(f'Cedulas de 20: {cedulas20}')

if valor >= 10:
    cedulas10 = valor // 10
    valor -= cedulas10 * 10
    print(f'Cedulas de 10: {cedulas10}')

if valor >= 5:
    cedulas5 = valor // 5
    valor -= cedulas5 * 5
    print(f'Cedulas de 5: {cedulas5}')

if valor:
    cedulas1 = valor
    print(f'Cedulas de 1: {cedulas1}')

