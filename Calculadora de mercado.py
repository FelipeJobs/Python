#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
soma = 0
cont = 0
produtos = []
precos = []
while True:
    nome = input("\33[33mQual é o nome do produto: ")
    preco = float(input("\33[34mQual é o preço do produto R$: "))
    continuar = input("\33[34mVocê deseja continuar? S/N: ").upper()
    soma = soma + preco
    precos.append(preco)
    produtos.append(nome)
    if preco > 1000:
        cont = cont +1
    if continuar == "N":
        break
print("-"*30)
print(f"\33[34mO total gasto na compra é: {soma}")
print(f"\33[35mExiste na sua lista de compra {cont} produtos que custam mais que R$ 1000.")
print(f"\33[36mO produto mais barato da sua lista é {produtos[precos.index(min(precos))]} que custa {min(precos)}")