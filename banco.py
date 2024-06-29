menu = """
BANCO - MENU

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

Digite uma opção => """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)

    #depositar
    if opcao == "1":
        valor = float(input("\nInforme o valor do depósito => "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("=> Deposito realizado com sucesso")

        else:
            print("ERROR: Valor inválido para depósito")
    
    # sacar
    elif opcao == "2":
        valor = float(input("\nInforme o valor do saque => "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("ERROR: Saldo insuficiente para saque")

        elif excedeu_limite:
            print("ERROR: Valor excede o limite de saque")

        elif excedeu_saques:
            print("ERROR: Número máximo de saques excedido")

        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
            print("=> Saque realizado com sucesso")

        else:
            print("ERROR: Valor inválido para saque")

    #extrato
    elif opcao == "3":
        print("\n===== EXTRATO =====")
        print("\n=> Nenhuma movimentação realizada" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")

        #if not extrato:
        #    print("\n=> Nenhuma movimentação realizada")
        #else:
         #   print(f"\nSaldo: R$ {saldo:.2f}")

        print("\n====================")

    #sair
    elif opcao == "4":
        print("\n=> Operação finalizada!\n")
        break

    else:
        print("\nERROR: Opção inválida")