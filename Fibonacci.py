numero = int(input("Digite um número: "))
a, b = 0, 1

while b <= numero:
    if b == numero:
        print(numero, "pertence à sequência de Fibonacci.")
        break
    a, b = b, a+b
else:
    print(numero, "não pertence à sequência de Fibonacci.")




