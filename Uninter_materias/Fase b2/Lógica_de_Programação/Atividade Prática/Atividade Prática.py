# Bem vindo a Loja do Matheus Garcia de Oliveira
print('Bem vindo a Loja do Matheus Garcia de Oliveira')

# Variáveis
total = 0
desconto = 0
valor_desconto = 0

# Inicio
valor_produto = float(input('Digite o valor da unidade: '))
qnt = int(input('Digite o valor da quantidade: '))

for i in range(qnt):
    total += valor_produto

if qnt >=5 and qnt <= 19:
    valor_desconto = 3

elif qnt >= 20 and qnt <= 99:
    valor_desconto = 6

elif qnt >= 100:
    valor_desconto = 10

desconto = (valor_desconto * valor_produto) / 100
desconto *= qnt
desconto -= total

print(f'Valor sem desconto: {round(total, 3)}')
print(f'Valor com desconto: {abs(round(desconto, 3))} (desconto {valor_desconto}%)')