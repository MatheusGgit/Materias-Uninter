# Matheus Garcia de Oliveira
print('Bem-vindo ao Controle de Estoque da Mercearia do Matheus Garcia de Oliveira')

# Variáveis
cont = 's'
produtos = {}
lista_produtos = []
codigo_produto = 0


# Funções
def cadastrarProduto(nomeP, fabricanteP, valorP, codigoP):
   produtos = {'Código': codigoP, 'Nome': nomeP, 'Fabricante': fabricanteP, 'Valor': valorP}
   lista_produtos.append(produtos)

def consultarProduto(escolha):
    if escolha == 1:
        print('Todos os produtos:')
        for i in (lista_produtos):
            print(i, '\n')

    elif escolha == 2:
        print('Consulta por codigo:')
        try:
            codigo_consulta = int(input('insira o código do produto: '))
            for i in range(len(lista_produtos)):
                if int(lista_produtos[i]['Código']) == codigo_consulta:
                    print(lista_produtos[i], '\n')
        except:
            print('Opção inválida')

    elif escolha == 3:
        print('Consulta por fabricante')
        try:
            fabricante_consulta = input('Insira o fabricante: ')
            for i in range(len(lista_produtos)):
                if lista_produtos[i]['Fabricante'] == fabricante_consulta:
                    print(lista_produtos[i], '\n')
        except:
            print('Opção inválida\n')

def removerProduto(codigoP):
    for i in range(len(lista_produtos)):
        if int(lista_produtos[i]['Código']) == codigoP:
            del lista_produtos[i]
            print('Produto removido!\n')


# Inicio - Função main
while cont == 's':
    print('1 - Cadastrar produto')
    print('2 - Consultar produto(s)')
    print('3 - Remover Produto')
    print('4 - Sair')
    try:
        escolha = int(input('>>> '))
        print()

    except:
        print('Opção inválida\n')
        continue

    if escolha not in (1, 2, 3, 4):
        print('Opção inválida\n')

    else:
        if escolha == 4:
           break

        elif escolha == 1:
            nome = input('Insira o nome do produto: ')
            fabricante = input('Insira o fabricante do produto: ')
            codigo_produto += 1

            inserirValor = True
            while inserirValor == True:
                try:
                    valor = float(input('Insira o valor do produto: '))
                    print()
                    break
                except:
                    print('Opção inválida\n')
                    continue

            cadastrarProduto(nome, fabricante, valor, codigo_produto)

        elif escolha == 2:
            print('1 - Consultar todos os produtos')
            print('2 - Consultar produto por codigo')
            print('3 - Consultar produto por fabricante')
            print('4 - Retornar')
            try:
                consulta = True
                while consulta == True:
                    escolhaConsulta = int(input('>>> '))
                    print()

                    if escolhaConsulta not in (1, 2, 3, 4):
                        print('Opção inválida\n')
                        continue
                    elif escolhaConsulta == 4:
                        break

                    else:
                        break
                consultarProduto(escolhaConsulta)

            except:
                print('Opção inválida\n')

        elif escolha == 3:
            try:
                codigo_produto = int(input('Insira o codigo do produto que deseja remover: '))
                removerProduto(codigo_produto)
            except:
                print('Opção inválida\n')