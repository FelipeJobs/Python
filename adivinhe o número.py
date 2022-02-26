#faça um programa que gere um número inteiro entre 0 a 10 e faça o usuário adivinhar, se ele
#acertar imprima na tela que ele ganhou.
import random
cont = 0
num = int(input("vou pensar num número entre 0 a 10 tente adivinhar qual é esse número: "))
aleatorio = random.randint(0,10)
while num != aleatorio:
   num = int(input("Infelizmente você errou tente novamente: "))
   cont = cont +1
if cont == 1:
   print("\33[34mVocê acertou com {} tentativa".format(cont+1))
elif cont > 1:
   print("\33[34mVocê acertou com {} tentativas".format(cont + 1))
