# faça um programa que mostre na tela a contagem regressiva para os fogos de artifícios. indo de 10 até 0.
# com uma pausa de 1 segundo entre eles
from time import sleep
inicio = int(input("Digite o valor do início da contagem: "))
fim = int(input("Digite o valor do fim da contagem: "))
for c in range(inicio,fim -1,-1):
    print(c)
    sleep(1)
print("Feliz ano novo!!!")