def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except:
        return False
    else:
        return True

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Ocorreu algum erro')
    else:
        print('Arquivo criado com sucesso')

def povoaArquivo(nomeArquivo, mensagem):
    try:
        a = open(nomeArquivo, 'at')
        a.write('\n' + mensagem)
        a.close()
        return True
    except:
        print('Ocorreu algum erro')

arquivo = 'arquivoAleatorio.txt'
if existeArquivo(arquivo):
    print('Localizado no computador')
    mensagem = input('Digite uma mensagem: ')
    if povoaArquivo(arquivo, mensagem):
        print('Mensagem escrita com sucesso')
else:
    print('Arquivo inexistente')
    criaArquivo(arquivo)

