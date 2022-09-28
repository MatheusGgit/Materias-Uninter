A = int(input('Digite o primeiro lado do triangulo: '))
B = int(input('Digite o segundo lado do triangulo: '))
C = int(input('Digite o terceiro lado do triangulo: '))

if A > 0 and B > 0 and C > 0:
    if (A + B > C) and (A + C > B) and (B + C > A):
        print('É um triangulo')
        if A != B and A != C and B != C:
            print('Triangulo escaleno!')
        elif A == B and A == C and B == C:
            print('Triangulo equilátero!')
        else:
            print('Triangulo isósceles')
    else:
        print('Não é um triangulo')
else:
    print('Por favor digite números adequados')