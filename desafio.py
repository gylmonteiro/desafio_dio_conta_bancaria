numero_deposito = 0
numero_saque = 0
quantidade_saque = 0
extrato = {}
saldo = 0


while True:
    print(
        "DIGITE (E) PARA EXTRATO\
        DIGITE (S) PARA SAQUE\
        DIGITE (D) PARA DEPOSITO\
        DIGITE (Q) PARA SAIR"
    )
    funcao = input("Digite a função desejada:").upper()

    if funcao == "E":
        print(f"Extrato {extrato} | Saldo atual: R${saldo:.2f}")
    elif funcao == "S":
        if quantidade_saque <= 3:
            valor = float(input("Digite o valor do saque:"))
            if valor > 500:
                print("Esse valor não é acima do permitido")
            elif valor < 0:
                print("Esse valor é abaixo do permitido")
            elif valor > saldo:
                print(f"Seu saldo é insuficiente. Saldo atual: {saldo}")
            else:
                quantidade_saque += 1
                numero_saque += 1
                extrato[f"saque_{numero_saque}"] = f"R$ {valor:.2f}"
                saldo -= valor
            print(f"Extrato {extrato} | Saldo atual: R${saldo}")

    elif funcao == "D":
        valor = float(input("Valor a ser depositado:"))
        if valor <= 0:
            print("O valor digitado não pode ser depositado")
        else:
            numero_deposito += 1
            extrato[f"deposito_{numero_deposito}"] = f"R$ {valor:.2f}"
            saldo += valor

        print(extrato)
    elif funcao == "Q":
        break

    else:
        print("Você não digitou uma opção válida")
