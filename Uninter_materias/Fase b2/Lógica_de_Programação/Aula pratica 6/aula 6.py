# soma de uma tupla sem saber a quantidade de parametros
print('soma de uma tupla sem saber a quantidade de parametros')
def soma(*num):
    soma = 0
    for i in num:
        soma += i
    return soma

res = soma(1, 2, 3, 4, 5)
print(f'Resultado: {res}')

res = soma(1, 2, 3, 4, 5, 6, 7, 8, 10)
print(f'Resultado: {res}')


# Fazendo um dicionario usando listas
print()
print('Fazendo um dicionario usando listas')
item = []
mercado = []

for i in range(1):
    item.append(input('Digite o nome do produto: '))
    item.append(input('Digite a quantidade de unidades: '))
    item.append(input('Digite o valor: '))
    mercado.append(item[:])
    item.clear()

print(mercado)

# Dicionarios
print()
print('Dicionarios')
teste = {'numero': '1', 'nome': 'teste', 'ano': '2000'}
print(teste)

# lista de dicionarios
print()
print('lista de dicionarios')
lista = []

teste = {'numero': '1', 'nome': 'teste', 'ano': '2000'}
teste2 = {'numero': '2', 'nome': 'teste2', 'ano': '2000'}
teste3 = {'numero': '3', 'nome': 'teste3', 'ano': '2000'}

lista.append(teste)
lista.append(teste2)
lista.append(teste3)

print(lista)