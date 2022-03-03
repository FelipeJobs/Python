# Faça um programa que jogue par ou ímpar com o computador.O jogo só será interrompido
# quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou
# no final do jogo.
import random
vitorias = -1
while True:
    jogador = int(input("Diga um valor: "))
    computador = random.randint(0,10)
    escolha = input("Você quer P/I: ").upper()
    soma = jogador + computador
    parouimpar = ""
    vitorias = vitorias + 1
    if soma % 2 == 0:
        parouimpar = "Par."
    elif soma % 2 != 0:
        parouimpar = "Ímpar."
    print(f"Você jogou {jogador} e o computador jogou {computador}. O total deu {soma} que é {parouimpar}")
    print("-"*20)
    if escolha == "P" and soma % 2 == 0:
        print("Você venceu!!\nVamos jogar navamente...")
        print("-" * 20)
    if escolha == "I" and soma % 2 != 0:
        print("Você venceu!!\nVamos jogar navamente...")
        print("-" * 20)
    if escolha == "P" and soma % 2 != 0:
        print("Você perdeu !!")
        print("-" * 20)
        break
    if escolha == "I" and soma % 2 == 0:
        print("Você perdeu !!")
        print("-" * 20)
        break
if vitorias <=1:
    print(f"Game Over !!!\nVocê consiguiu {vitorias} vitória consecutiva.")
elif vitorias >1:
    print(f"Game Over !!!\nVocê consiguiu {vitorias} vitórias consecutivas.")


