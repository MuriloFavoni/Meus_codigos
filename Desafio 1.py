import textwrap

menu = """
=======MENU=======
[1]\tDepositar
[2]\tSacar
[3]\tExtrato
[4]\tNova conta
[5]\tListar contas
[6]\tNovo usuário
[7]\tSair
==================
"""

saldo = 0
limite = 500
extrato = ""
quant_saque = 0
usuarios = []
contas = []
LIMITE_SAQUES = 3
AGENCIA = "0001"

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR${valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nOperação falhou! Valor inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, quant_saque, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = quant_saque > LIMITE_SAQUES
    
    if excedeu_saldo:
            print("\nOperação falhou! Saldo suficiente.")
            
    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque é excedeu o limite.")
        
    elif excedeu_saques:
        print("\nOperação falhou! Quantidade máxima de saques atingida.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR${valor:.2f}\n"
        quant_saque += 1
        print("\nSaque realizado com sucesso!")

    else:
        print("\nOperação falhou! O valor informado é inválido.")

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe um usuário com este CPF.")
        return
  
    nome = input("Informe seu nome completo: ")
    data_nasc = input("Infome sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (logradouro, número - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nasc": data_nasc, "cpf": cpf, "endereco": endereco})
    
    print(f"Usuário criado com sucesso, seja bem vindo {nome}!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuarios:
        print("\nConta criada com sucesso!")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Tituar:\t{conta['usuario']['nome']}
        """
        print("=" + 100)
        print(textwrap.dedent(linha))

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Digite o valor do deposito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == 2:
        valor = float(input("Digite o valor do saque: "))
        saldo, extrato = sacar(
           saldo=saldo,
           valor=valor,
           extrato=extrato,
           limite=limite,
           quant_saque=quant_saque,
           LIMITE_SAQUES=LIMITE_SAQUES
       )
        
    elif opcao == 3:
        exibir_extrato(saldo,extrato=extrato)

    elif opcao == 4:
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == 5:
        listar_contas(contas)

    elif opcao == 6:
        criar_usuario(usuarios)

    elif opcao == 7:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")