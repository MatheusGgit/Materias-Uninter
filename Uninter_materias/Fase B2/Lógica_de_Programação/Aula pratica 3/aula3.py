# Condicionais
# A)
print('### A ###')
if 2 + 2 < 4 or 2 + 2 > 4:
    print('True')
else:
    print('False')

# B)
print()
print('### B ###')
if 7 // 3 == 1 + 1:
    print('True')
else:
    print('False')

# C)
print()
print('### C ###')
if (3 ** 2 and 4 ** 2) == 25:
    print('True')
else:
    print('False')

# D)
print()
print('### D ###')
if 2 + 4 + 6 > 12:
    print('True')
else:
    print('False')

# E)
print()
print('### E ###')
try:
    ano = int(input('Digite um ano: '))
    if ano % 4 == 0:
        print('Pode ser um ano bissexto')
    else:
        print('Definitivamente não é um ano bissexto')
except:
    pass
# F)
print()
print('### F ###')
cima = True
baixo = False
if cima and baixo:
    print('Decida-se!')
else:
    print('Você escolheu um caminho!')

# G)
# H)