import math

def fatorial(num):
    fat = 1
    if num == 0:
        return fat
    else:
        for i in range(1, num + 1):
            fat *= i
    return fat

def fatorialBiblioteca(num):
    fat = math.factorial(num)
    return fat


num = int(input('Digite um valor para ser fatorado: '))
fat = fatorial(num)
print(f'Fatoração: {fat}')

# Ou
print()
num = int(input('Digite um valor para ser fatorado: '))
fat = fatorialBiblioteca(num)
print(f'Fatoração: {fat}')