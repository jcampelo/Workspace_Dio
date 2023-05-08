
import sys
#Com duas duas condicões if and else
"""
saldo = 2000.0

saque = float (input ("Infome o valor do saque:"))

if saldo >= saque:
    print ("Realizando saque")

else:
    print("Saldo insfuficiente!")

"""
# if / elif / else

"""
opcao = int(input("Informe uma opcao: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))

elif opcao == 2:
    print ("Exibindo o extrato ....  ")

else:
    sys.exit("Opção invalida")
"""
"""
IDADE_ESPECIAL = 17
MAIOR_IDADE = 18

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print ("Você tem {} anos e pode tirar CNH".format(idade))

if idade < MAIOR_IDADE:
    print ("Você tem {} anos e não pode tirar CNH".format(idade))

if idade >= MAIOR_IDADE:
    print ("Você tem {} anos e pode tirar CNH".format(idade))

else:
    print ("Você tem {} anos e não pode tirar CNH".format(idade))


if idade >= MAIOR_IDADE:
    print ("Você tem {} anos e pode tirar CNH".format(idade))

elif idade == IDADE_ESPECIAL:
    print ("Você tem {} anos e pode fazer aulas teoricas, mas não pode fazer aulas práticas".format(idade))

else:
    print ("Você tem {} anos e não pode tirar CNH".format(idade))
"""

