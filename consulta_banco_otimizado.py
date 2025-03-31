
import textwrap as tw



def menu():

    menu = """\n

    ====================MENU====================

    [d] depósito
    [s] saque
    [e] extrato
    [nc] nova conta
    [lc] listar contas
    [nu] novo usuário
    [q] sair

    =>
    """
    return input(tw.dedent(menu))


def depositar(saldo,valor,extrato, /):
    if valor > 0:
        saldo += valor
        extrato = (f'Depósito de R${valor:.2f}')
        print(f'Depósito de R${valor:.2f}')
    else:
        print('Operação inválida, tente outra opção')
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques < limite_saques:
        if valor <= saldo:
            if valor > 0 and valor <= limite:
                saldo -= valor
                extrato = (f'Saque de R${valor:.2f}')
                print(f'Saque de R${valor:.2f}')
            elif valor > limite:
                print('Limite máximo de R$500,00 por transação')
        else:
            print('Saldo insuficiente')
    else:
        print('Número máximo de saques diários atingido')
    return saldo, extrato


def exibir_extrato(saldo,/,*, extrato):
    print("================EXTRATO DE HOJE================")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo: {saldo:.2f}")
    print("================FIM================")

def criar_usuario(usuarios): 
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf=cpf, usuarios=usuarios)
    if usuario:
        print("Usuário já cadastrado")
        return
    nome = input("Informe o nome do usuário: ")
    nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro,nro - bairro - cidade/sigla estado): ")
    usuarios.append({"cpf": cpf, "nome": nome, "nascimento": nascimento, "endereco": endereco})
    print("Usuário criado com sucesso")

def filtrar_usuario(cpf, usuarios): 
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios): 
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf=cpf, usuarios=usuarios)
    if usuario:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("Usuário não encontrado")
        return None


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência: {conta['agencia']}
        C/C: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        """
        print("="*40)
        print(tw.dedent(linha))
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "nu": 
            criar_usuario(usuarios)
            print("Usuário criado com sucesso")
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
            print("Conta criada com sucesso")
        elif opcao == "lc":
            listar_contas(contas) 
            print("Contas listadas com sucesso")
        elif opcao == "q":
            break
            print("Sistema encerrado")
        else:
            print("Operação inválida, tente outra opção")


main()
# Código otimizado para o sistema bancário