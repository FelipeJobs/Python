#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os
# dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
continuar = 'S'
dados = []
dado = {}
cont = 0
media = 0
while continuar == "S":
    dado['Nome'] = input('Nome: ')
    dado['Idade'] = int(input('Idade: '))
    dado['Sexo'] = input('Sexo M/F: ').upper()
    dados.append(dado.copy())
    cont = cont +1
    media = media + dado['Idade']
    continuar = input('\nDeseja cadastrar outra pessoa S/N: ').upper()
print('-='*45)
print(f'\33[33mForam cadastradas {cont} pessoas.')
print('-='*45)
print(f'\33[34mA média das idades cadastradas é: {media//cont}')
print('-='*45)
print('\33[35mO nome de todas as mulheres cadastradas São:')
for c in range(0,len(dados)):
    if dados[c]['Sexo'] == 'F':
        print(dados[c]['Nome'])
print('-='*45)
print('\33[36mAs pessoas que possuem idade maior do que a média geral São:')
for c in range(0,len(dados)):
    if dados[c]['Idade'] > media//cont:
        print(dados[c]['Nome'])
print('-='*45)