# faça um programa que leia o comprimento do cateto oposto e
#adjascente de um triângulo retângulo e calcule a sua hipotenusa.
import math
catetoO= int(input("Digite o valor do cateto oposto do triângulo: "))
catetoA= int(input('Digite o valor do cateto adjascente do triângulo: '))
hipotenusa= math.hypot(catetoA,catetoO)
print('O valor da hipotenusa desse triângulo é:{}'.format(hipotenusa))

