#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os
# valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
# geradas.
numero = []
par = []
impar = []
while True:
    print('\33[31mCaso queira parar o programa basta digitar 0.')
    digitar = int(input('\33[36mDigite o valor de um número inteiro:'))
    if digitar == 0:
        break
    numero.append(digitar)
    if digitar % 2 == 0:
        par.append(digitar)
    else:
        impar.append(digitar)
print('-='*45)
print(f'''\33[33mNúmeros digitados:
{numero}''')
print('-='*45)
print(f'''\33[34mTodos os números digitados que são pares:
{par}''')
print('-='*45)
print(f'''\33[35mTodos os números ímpares digitados São:
{impar}''')
print('-='*45)