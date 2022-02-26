#Crie um programa que leia nome e duas notas de vários alunos e
# guarde tudo em uma lista composta. No final, mostre um boletim
# contendo a média de cada um e permita que o usuário possa mostrar
# as notas de cada aluno individualmente.
dados = []
dado = []
cadastro = 'S'
media = []
while cadastro == 'S':
    nome = str(input('Nome do aluno: '))
    notaum = float(input('Nota 1: '))
    notad = float(input('Nota 2: '))
    dado.append(nome)
    dado.append(notaum)
    dado.append(notad)
    dados.append(dado[:])
    dado.clear()
    media.append(float(notaum+notad)//2)
    cadastro = input('''Os dados foram cadastrados com sucesso
Você deseja cadastrar outra pessoa S/N? ''').upper()
print('-='*45)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-='*45)
for i,a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{media[i]:>8}')
print('-='*45)
while True:
    posicao = 0
    posicão = (int(input('Caso queira finalizar o programa basta digitar 999\nDigite o número do aluno que deseja verificar as notas: ')))
    if posicão == 999:
        break
    print(dados[posicão][1:3])
print('\33[36mPrograma finalizado.\nTenha um ótimo dia!!!')


