nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

# OLD STYLE %
print ( " ########   NO METODO OLD STYLE ##########\n")
print ("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s.\n" % (nome , idade, profissao, linguagem))

# METODO FORMAT 
print ( "########## NO METODO FORMAT ########\n")

print ("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}." .format (nome , idade, profissao, linguagem))
print ("Olá, me chamo {2}. Eu tenho {3} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.\n" .format (linguagem , profissao, nome, idade))

# f - String
print ( "########## NO METODO f-string ########\n")
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no de linguagem {linguagem}\n")

# FORMATAR STRINGS COM f -strings

PI = 3.14159
print(f"Valor de PI: {PI:.2f}") # irei passar duas casas depois da virgula
print(f"Valor de PI: {PI:10.2f}") # irei passar 10 casas antes da virgual


