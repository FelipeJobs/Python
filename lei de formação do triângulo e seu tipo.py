# Desenvolva um programa que leia o comprimento de 3 retas e informe se
#é possível formar um triângulo.
#abs retorna o valor absoluto, ou seja, em modulo.
a = int(input("Digite o valor do comprimento da primeira reta: "))
b = int(input("Digite o valor do comprimento da segunda reta: "))
c = int(input("Digite o valor do comprimento da terceira reta: "))
if abs(b-c) < a and abs(b+c) > a:
    print("é possível formar um triângulo com essas 3 retas e ele é: ")
else:
    print("Não é possível formar um triângulo com essas retas.")
if a == b == c:
    print("Equilátero")
elif a == b or a == c:
    print("Isósceles")
else:
    print("Escaleno")