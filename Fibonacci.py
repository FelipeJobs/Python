#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
# elementos de uma Sequência de Fibonacci.
termos = int(input("\33[34mQuantos termos você gostaria que tivesse a sequência de fibonacci? "))-2
inicio = 0
fim = 1
contador = 0
while contador < termos:
    if inicio == 0 and fim == 1:
        print("0 - 1 -",end=" ")
    sequencia = inicio + fim
    contador = contador + 1
    inicio = fim
    fim = sequencia
    print("{} - ".format(sequencia),end="")
print("\33[31mFim")