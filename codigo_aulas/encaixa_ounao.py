N = int(input("Entre com um valor:"))

while(N > 0):
  a, b = input().split()
  if a[-len(b):] == b:
    print("encaixa")
  else:
    print("nao encaixa")
  N -= 1
    