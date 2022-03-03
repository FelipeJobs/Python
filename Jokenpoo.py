# crie um programa que faça o computador jogar jokenpo com você.
import random
from time import sleep
escolha = int(input("Suas opções são:\n 1= Pedra\n 2= Papel\n 3= Tesoura\n Qual a sua jogada: "))
print("Jo")
sleep(1)
print("Ken")
sleep(1)
print("Po!!!")
Pedra = 1
Papel = 2
Tesoura = 3
computador =[Pedra,Papel,Tesoura]
computadores = random.choice(computador)
print("-="*14)
if computadores == 1:
    print("Escolha da máquina: Pedra")
elif computadores == 2:
    print("Escolha da máquina: Papel")
elif computadores == 3:
    print("Escolha da máquina: Tesoura")
if escolha == 1:
    print("A sua escolha foi: Pedra")
elif escolha == 2:
    print("A sua escolha foi: Papel")
elif escolha == 3:
    print("A sua escolha foi: Tesoura")
else:
    print("Jogada inválida, escolha uma opção válida")
print("-="*14)
if escolha == computadores:
    print("Deu empate tente novamente.")
elif escolha == 1 and computadores == 3 or escolha == 3 and computadores == 2 or escolha == 2 and computadores == 1:
    print("Você venceu.")
elif computadores == 1 and escolha == 3 or computadores == 2 and escolha == 1 or computadores == 3 and escolha == 2:
    print("O computador venceu.")

