km = float(input('Quantos km foram percorridos: '))
dia = int(input('Por quantos dias ele foi alugado: '))

preco = 60 * dia + 0.15 * km
print(f'Km = {km}')
print(f'Dias: {dia}')
print(f'Valor a ser pago: {preco}')