# Lista que irá armazenar os produtos
estoque = []

# Função que irá cadastrar os produtos
def cadastrar_produto():
    print("\n=== CADASTRAR PRODUTO ===")

    codigo = input("Digite o código do produto: ")

    # Verificar código duplicado
    for produto in estoque:
        if produto["codigo"] == codigo:
            print("Erro: já existe um produto com esse código.")
            return

    nome = input("Digite o nome do produto: ")

    # Validação do preço do produto
    while True:
        try:
            preco = float(input("Digite o preço do produto: "))
            if preco < 0:
                print("O preço não pode ser negativo.")
            else:
                break
        except ValueError:
            print("Digite um valor válido para o preço.")

    # Validação da quantidade do produto
    while True:
        try:
            quantidade = int(input("Digite a quantidade do produto: "))
            if quantidade < 0:
                print("A quantidade não pode ser negativa.")
            else:
                break
        except ValueError:
            print("Digite um valor válido para a quantidade.")

    # Criando descrições do produto
    produto = {
        "codigo": codigo,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    # Adicionando à lista
    estoque.append(produto)

    print("Produto cadastrado com sucesso!")


# Função para calcular total de produtos
def calcular_total_produtos():
    total = 0

    for produto in estoque:
        total += produto["quantidade"]

    print(f"\nQuantidade total de produtos em estoque: {total}")


# Função para exibir menu
def menu():
    while True:
        print("\n=== SISTEMA DE CONTROLE DE ESTOQUE ===")
        print("1 - Cadastrar Produto")
        print("2 - Calcular Total de Produtos em Estoque")
        print("3 - Listar Produtos")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()

        elif opcao == "2":
            calcular_total_produtos()

        elif opcao == "3":
            print("\n=== PRODUTOS CADASTRADOS ===")

            if len(estoque) == 0:
                print("Nenhum produto cadastrado.")
            else:
                for produto in estoque:
                    print(f"""
Código: {produto['codigo']}
Nome: {produto['nome']}
Preço: R$ {produto['preco']:.2f}
Quantidade: {produto['quantidade']}
-----------------------------""")

        elif opcao == "4":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Execução do programa
menu()