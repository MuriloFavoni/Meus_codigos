estoque = []
total_geral = 0
while True:
    menu = int(input("""
    [1] Cadastrar produtos
    [2] Buscar produtos
    [3] Estoque
    [4] Retirar produto
    [5] Sair
    \n"""))
    if menu == 1:
        print("===Cadastrar Proutos===")
        cadastro = int(input("Produtos a cadastrar: "))
        for _ in range(cadastro):
            nome = input("\nNome do produto: ").title()
            preco = float(input("Preço unitário: R$ "))
            qtd = int(input("Quantidade em estoque: "))
            produto = (nome, preco, qtd)
            estoque.append(produto)
            print(f"Valor total de {nome}: R${preco * qtd:.2f}\n")
            total_geral += preco * qtd
        print(f"Valor total do estoque: R${total_geral:.2f}\n")
        print("=======================")
    elif menu == 2:
        print("===Buscar Produtos===")
        busca = input("\nProduto: ").title()
        for nome, preco, qtd in estoque:
            if busca == nome:
                print(f"Preço: R${preco:.2f}")
                print(f"Estoque: {qtd} unidades\n")
                break
        else:
                print("Produto não cadastrado.\n")   
        print("=====================") 
    elif menu == 3:
            print("===Produtos Sem Estoque===")
            for nome, preco, qtd in estoque:
                if qtd == 0:
                    print(f"{nome} está fora de estoque.\n")
                else:
                    print("Todos os produtos cadastrados tem estoque.")
            print("==========================")
    elif menu == 4:       
        print("===Retirada===")
        retira = input("Produto: ").title()
        qtd_retira = int(input("Quantidade: "))
        for i, (nome,preco, qtd) in enumerate(estoque):
            if retira == nome:
                if qtd_retira <= qtd:
                    estoque[i] = (nome, preco, qtd - qtd_retira)
                    print(f"Tem {qtd - qtd_retira} unidades de {nome} no estoque agora.")
                else:
                    print("Não tem essa quantidade no estoque.")
        print("==============")
    elif menu == 5:
        print("Sistema encerrado.")
        break
    else:
        print("Número inválido.")