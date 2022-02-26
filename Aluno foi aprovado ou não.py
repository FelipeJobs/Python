#Faça um programa que leia nome e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo da estrutura na tela.
nome = input('Qual é o nome do aluno: ')
media = int(input("Qual é a média desse aluno: "))
situacao = ''
if media >=7:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'
dados = {'Nome':nome, 'Media': media, 'Situação':situacao}
for i,c in dados.items():
    if i == 'Media' or i == 'Situação':
        print(f'A {i} é igual {c}')
        continue
    print(f'O {i} é igual {c}')

