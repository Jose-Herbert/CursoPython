"""

Faça uma lista de compras com lista
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
não permita que o progama quebre com erros de indices inexistentes na lista

"""
import os

lista_compras = []
pedir_sair = False


while pedir_sair == False:
    # Print do header
    print('Qual ação deseja realizar?')
    print('(a)dicionar  (r)emover  (l)istar (s)air')
    # ação que o cliente pode tomar dentre as disponiveis acima, .lower() vai sempre deixar o input em lowercaps
    acao_realizada = input('').lower()

    # se acao_realizada for igual a "a"
    if acao_realizada == 'a':
        adicionar = True
        # enquanto adicionar for verdadeiro ele ira executar a ação de pedir um produto novo para ficar adicionando á lista
        while adicionar:
            os.system('clear')
            print('Qual Produto você vai querer Adicionar?')
            adicionar_produto = input('').strip().lower()
            os.system('clear')
            print(f'Produto Adicionado (produto: {adicionar_produto})')
            print(' ')
            # Ação do cliente para quebrar o while
            print('Você deseja sair? (s)im')
            sair = input('').lower()
            # se len(adicionar_produto) for menor que 1 ele ira printar uma informação para adicionar um produto
            if adicionar_produto == '' or adicionar_produto == ' ':
                print('Porfavor Adicionar um Produto...')
            else:
                lista_compras.append(adicionar_produto)
            
            # se o input for igual ao 's' ele ira quebrar o loop do while
            if sair == 's':
                print('Saindo...')
                print(' ')
                adicionar = False
            else:
                ...

        # se acao_realizada for igual a 'r' ele irá remover um item da lista_compras pelo index
    elif acao_realizada == 'r':
        try:
            os.system('clear')
            for item in enumerate(lista_compras):
                print(item)
            id_para_remover = input('Digite o id do item: ')
            print(' ')
            id = int(id_para_remover)
            del lista_compras[id]
            print(lista_compras)
        except:
            print('Esse id não existe na lista')

        # se acao_realizada for igual a 'l' ele irá listar os produtos da lista_compras
    elif acao_realizada == 'l':
        os.system('clear')
        print('Você comprou os seguintes items:')
        # essa variável contem um dicionario que contem em tupla a contagem de quantidade de item na memória e o item para cada item na lista_compras
        qnt_item = {
            (lista_compras.count(item), item)
            for item in lista_compras
        }
        # esse laço cria uma interavel de tupla(t) no dicionario de qnt_item que lista os item de quantidade e o string do item
        for t in qnt_item:
            quantidade, item = t
            print(f'Item: {item}, Quantidade: {quantidade} ')
            print(' ')
        
        # se acao_realizada for igual a 's' ele quebra o while pedir_sair == False: inicial e 'fecha' o progama a partir do while
    elif acao_realizada == 's':
        os.system('clear')
        pedir_sair = True


    else:
        os.system('clear')
        print('Porfavor digitar apenas as Ações Disponíveis!!')
        print(' ')