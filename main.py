# @title Treinando Logica De Programação
lista_livro = {}

while True:
    print("Listador De Livros")
    print("1 - Adicionar Livro")
    print("2 - Consultar Livro")
    print("3 - Remover Livro")
    print("4 - Exibir Todos Os Livros ")
    print("5 - Sair")

    opcao = int(input("Opção: "))

    if opcao == 1:
        titulo = str(input("Titulo Do Livro: "))
        autor = str(input("Nome Do Autor: "))
        ano = int(input("Ano De Publicação: "))
        paginas = int(input("Número De Paginas: "))

        lista_livro[titulo] = {"autor":autor,"ano_publicacao":ano,"num_paginas":paginas}
        continue
    elif opcao == 2:
       nome_titulo = str(input("Digite o titulo do livro Para Buscar: "))

       if nome_titulo in lista_livro:
            print("-"*25)
            print("Titulo: ",nome_titulo)
            print("Autor: ",lista_livro.get(nome_titulo)["autor"])
            print("Ano De Publicação: ",lista_livro.get(nome_titulo)["ano_publicacao"])
            print("Numero De Paginas: ",lista_livro.get(nome_titulo)["num_paginas"])
            print("-"*25)
            continue
       else:
            print("Livro Não Existe ou Foi Excluido")
            continue
    elif opcao == 3:
       nome_titulo = str(input("Digite o titulo do livro Para Remover: "))
       del lista_livro[nome_titulo]
       print(f"Livro: {nome_titulo} Removido Com Sucesso!")
       continue
    elif opcao == 4:
        if len(lista_livro) == 0:
            print("Não Possui Livros Para Listar")
            continue
        else:
            print("Listagem De Todos Os Livros")
            for chave, info in lista_livro.items():
                print("-" * 40)
                print(f"Titulo: {chave}")
                print(f"Autor: {info['autor']}")
                print(f"Ano De Publicação: {info['ano_publicacao']}")
                print(f"Número De Paginas: {info['num_paginas']}")
                continue
    elif opcao == 5:
        print("Programa Finalizado!")
        break


