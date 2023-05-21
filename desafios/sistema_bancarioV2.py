import textwrap

def menu(): #criando uma função menu

    menu = """\n
    ============= MENU GERAL ============

    [d]\tDEPOSITAR
    [s]\tSACAR
    [e]\tEXTRATO
    [nc]\tNOVA CONTA
    [lc]\tLISTAR CONTAS
    [nu]\tNOVO USUÁRIO
    [q]\tSAIR
    
        
    ==> """
    return input(textwrap.dedent(menu))

def depositar (saldo, valor, extrato,/): #recebendo argumentos somente por posição
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n === DEPÓSITO REALIZDO COM SUCESSO! ===")
    else:
        print("\n@@@ OPERACÃO FALHOU! O VALOR INFORMADO É INVÁLIDO. @@@")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques): #recebendo arumento por chave(keyword only)
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ OPERACÃO FALHOU! SALDO INSUFICIENTE !!! @@@")

    elif excedeu_limite:
        print("\n@@@ OPERACÃO FALHOU! O VALOR DO SAQUE EXCEDEU O LIMITE !!!. @@@")
    
    elif excedeu_saques:
        print("\n@@@ OPERACÃO FALHOU! EXCEDE OS SAQUES MAXIMO !!! @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:,2f}\n"
        numero_saques += 1
        print("\n === SAQUE REALIZADO COM SUCESSO! ===")

    else:
        print("\n @@@@ OPERACAO FALHOU! O VALOR INFORMADO PE INVÁLIDO !!!. @@@")


    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato): #receber os argumentos de forma posicional e também nomeada (keyword)
    print("\n ==========  EXTRATO ============")
    print("NÃO FORAM REALIZADAS MOVIMENTAÇÕES." if not extrato else extrato)
    print(f"\nSALDO:\t\tR$ {saldo:.2f}")
    print("=================================")
    
def criar_usuario(usuarios):
    cpf = input("INFORME O CPF (somente números):")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n JÁ EXISTE USUÁRIO COM ESSE CPF! @@@")
        return
    
    nome = input("INFORME O NOME COMPLETO: ")
    data_nascimento = input("INFORME A DATA DE NASCIMENTO (dd-mm-aaaa):  ")
    endereco = input(" INFORME O ENDEREÇO (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print (" ####### USUÁRIO CRIADO COM SUCESSO ######### ")


def filtrar_usuario(cpf, usuarios):
    ususarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return ususarios_filtrados[0] if ususarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("INFORME O CPF DO USUÁRIO: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print ("\n ########### CONTA CRIADA COM SUCESSO !!! #########")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario, "cpf":cpf}
    
    print ("\n USUÁRIO NÃO ENCONTRADO, FLUXO DE CRIAÇÃO DE CONTA ENCERRADO! @@@@@")        
    

def listar_contas(contas):
    for conta in contas:
        linha = f""" 

        AGÊNCIA:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        TITULAR:\t{conta['usuario'] ['nome']}
        CPF:\t{conta['cpf']}    
        DATA DE NASCIMENTO:\t{conta['usuario'] ['data_nascimento']}
        ENDEREÇO:\t{conta['usuario'] ['endereco']}
                
        
        """  # foi adicionado no report de contas os dados adicionais do usuario como cpf, nascimento.....
        print ("=" * 100)
        print (textwrap.dedent(linha))

    if contas == []:
        print ("NÃO HÁ CONTAS CADASTRADAS - PROSSIGA PARA OPÇÃO *NC NO MENU!!!") # adicionada para reportar que não há contas cadastradas

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
            valor = float(input("INFORME O VALOR DO DEPÓSITO:  "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("INFORME O VALOR DO SAQUE:  "))
            saldo, extrato = sacar(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                limite=limite,
                numero_saques=numero_saques,
                limite_saques= LIMITE_SAQUES,
                
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("OPÇÃO INVÁLIDA")

main()






