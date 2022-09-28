nomes = ('Maria', 'Luis', 'Romario', 'Alexandre')
cont = 0

for i in nomes:
    cont += 1
    print(f'Palavra {cont}: {i}')
    print('Vogais: ', end='')
    for j in i:
        if j.lower() in 'aeiou':
            print(j, ' ', end='')
    print('\n')

