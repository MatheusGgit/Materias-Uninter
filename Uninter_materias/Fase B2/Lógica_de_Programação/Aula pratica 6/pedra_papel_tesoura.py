
import random
pontosP1 = 0
pontosBot = 0

for i in range(3):
    print('Selecione uma das opções: ')
    print('1 - Pedra')
    print('2 - Papel')
    print('3 - Tesoura')
    escolha = int(input('Escolha: '))

    if escolha != 1 and escolha != 2 and escolha != 3:
        print('Por favor escolha uma opção valida')
        i -= 1
    else:
        bot = random.randint(1, 3)
        if escolha == 1: # Pedra
            if bot == 1:
                print('Empate!')
            elif bot == 2:
                print('Perdeu!')
                pontosBot += 1
            else:
                print('Ganhou!')
                pontosP1 += 1
            print()

        elif escolha == 2: # Papel
            if bot == 1:
                print('Ganhou!')
                pontosP1 += 1
            elif bot == 2:
                print('Empate!')
            else:
                print('Perdeu!')
                pontosBot += 1
            print()

        else: # Tesoura
            if bot == 1:
                print('Perdeu!')
                pontosBot += 1
            elif bot == 2:
                print('Ganhou!')
                pontosP1 += 1
            else:
                print('Empate!')
            print()

print(f'Pontos do bot: {pontosBot}')
print(f'Seus pontos: {pontosP1}')

if pontosBot > pontosP1:
    print('Você perdeu!')
elif pontosP1 == pontosBot:
    print('Empate!')
else:
    print('Você ganhou!')