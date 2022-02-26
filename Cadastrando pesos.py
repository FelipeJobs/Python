#Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
pessoas = []
escolha = 'S'
cont = 0
pesadas = []
leves = []
dados = []
pesos =[]
while escolha == 'S':
    dado = input("Qual é o seu nome? ")
    dados.append(dado)
    peso = int(input('Qual é o seu peso atual? '))
    pesos.append(peso)
    escolha = input("Você quer continuar S/N").upper()
    cont = cont + 1
    if escolha != 'S' and escolha != 'N':
        print("O valor digitado está incorreto tente novamente.")
        escolha = input("Você quer continuar S/N").upper()
        cont = cont -1
        dados.remove(dado)
        pesos.remove(peso)
        continue
    if peso > 70:
        pesadas.append(dado)
    if peso <= 70:
        leves.append(dado)
pessoas.append(dados)
pessoas.append(pesos)
print('-=' * 50)
print(f'Foram cadastrada {cont} pessoas no total.')
print('-=' * 50)
print(f'As pessoas mais leves do grupo, considerando aquelas que 70Kg ou menos são\n{leves}')
print('-=' * 50)
print(f'As pessoas mais pesadas do grupo, considerando aquelas que possuem mais de 70 kg são\n{pesadas}')
print('-=' * 50)