menu = '''

[d] depósito
[s] saque
[e] extrato
[q] sair

=>
'''
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES =3




while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Digite o valor do seu depósito: \n"))
        if deposito > 0:
            saldo+=deposito
            extrato += f"Depósito R$ {saldo:.2f}\n"
            print(f"depósito de R$ {deposito:.2f}")
            
        else:
            print("Operação inválida, tente outra opção")
    elif opcao == "s":
        saque = float(input("Digite o valor do seu saque: \n"))
        
        if numero_saques < 3 or saque > saldo :
            if saque > 0 and saque <= 500:
                saldo-=saque
                numero_saques+=1
                print(f"saque de R$ {saque}, numero de saque : {numero_saques} ")
                extrato += f"Saque R$ {saldo:.2f}\n"
            elif saque>500 :
                print("Limite máximo de R$ 500,00 por transação")
                numero_saques=3
        else:
            print("Número máximo de saques diários") 
            numero_saques=3   
    elif opcao == "e":
        print("================EXTRATO DE HOJE================")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: {saldo:.2f}")
        print("================FIM================")

    elif opcao == "q":
        break

    else :
        print("Operação inválida, tente outra opção")