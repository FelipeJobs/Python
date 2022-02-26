# faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
n1 = int(input("Digite um número inteiro de 0 a 9999: "))
unidade = n1 %10
dezena = n1//10%10
centana = n1//100 %10
milhar = n1//1000 %10
print('analisando o número {}'.format(n1))
print("Unidade: {}\n Dezena: {}\n Centena: {}\n Milhar: {}".format(unidade,dezena*10,centana*100,milhar*1000))
# é assim que utiliza o resto de um número para resolver esse desafio.