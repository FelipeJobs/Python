#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
# quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um
# dicionário, incluindo o total de gols feitos durante o campeonato.
nome = input('Nome do jogador: ')
partidas = int(input('Quantas partidas foram jogadas? '))
dados = {}
dados['Nome'] = nome
dados['Paritdas'] = partidas
gol = []
soma = 0
for c in range(1,partidas +1):
    gols = int(input(f'Quantos gols foram feitas na {c}º partida? '))
    gol.append(gols)
    dados['Gols'] = gol
    soma = soma + gols
    dados['Total de gols'] = soma
print('-='*40)
print(dados)
print('-='*40)
print(f'\33[35mO jogador {nome} jogou {partidas} partidas')
for c in range(1,partidas +1):
    print(f'\33[36m          => Na partida {c}º o jogador {nome} marcou {gol[c-1]}')
print(f"\33[34m          => O Total de gols marcados foram {dados['Total de gols']}")
