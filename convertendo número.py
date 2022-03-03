# escreva um programa que peça para o usuário digitar um número e
#escolher se ele será convertido para binário, octal ou hexadecimal.
n1 = int(input("Digite o valor que gostaria de converter: "))
conversao = int(input("Você gostaria de converter o número para: \n 1= binario\n 2= octal\n 3= hexadecimal\n digite o valor desejado: " ))
binario = bin(n1)
octal = oct(n1)
hexadecimal = hex(n1)
if conversao >=4:
    print("Opção inválida, digite uma opção válida.")
elif conversao == 1:
    print(binario)
elif conversao == 2:
    print(octal)
else:
    print(hexadecimal)

