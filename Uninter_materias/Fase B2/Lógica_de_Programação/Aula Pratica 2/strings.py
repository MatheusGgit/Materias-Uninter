# Divide a string pela metade e imprime os 2 ultimos numeros
frase = input('Digite um texto qualquer: ')
tam = len(frase)

frase2 = frase[:int(tam/2)]
print(frase2[-2:])

