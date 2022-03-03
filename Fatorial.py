#Faça um programa que leia um número qualquer e mostre o seu fatorial.
from math import factorial
sair = "N"
while sair == "N":
    numero = int(input("\nDigite o número que deseja saber o seu fatorial: "))
    print("\33[34mO fatorial do número {} é: {}\n".format(numero, factorial(numero)))
    sair = input("\33[36mVoce Deseja sair S/N: ").upper()
print("Obrigado por utilizar o nosso programa, tenha um ótimo dia!!!")


