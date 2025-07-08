menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""

saldo = 0
limite = 500
extrato = ""
quant_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Digite o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("Operação falhou! Valor inválido.")
        
    elif opcao == 2:
        valor = float(input("Digite o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = quant_saque >= LIMITE_SAQUES
        if excedeu_saldo:
            print("Operaçã falhou! Saldo suficiente.")
            
        elif excedeu_limite:
            print("Operação falhou! O valor do saque é excedeu o limite.")
        
        elif excedeu_saques:
            print("Operação falhou! Quantidade máxima de saques atingida.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            quant_saque += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == 4:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")