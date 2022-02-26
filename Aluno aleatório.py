#Um professor quer sortear um dos seus 4 alunos para apagar o quadro.
#Faça um programa que leia o nome deles e mostre o escolhido.
# eu posso usar random.choice para escolher um dado em uma lista
import random
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3= input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o número do quarto aluno: ")
sorteio = random.randint(1,4)
if sorteio == 1:
    print("O aluno escolhido para apagar o quadro foi "+ aluno1)
elif sorteio == 2:
    print('O aluno escolhido para apagar o quadro foi '+ aluno2)
elif sorteio == 3:
    print('O aluno escolhido para apagar o quadro foi '+ aluno3)
elif sorteio == 4:
    print('O aluno escolhido para apagar o quadro foi '+ aluno4)
# outra forma de resolver a questão.
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3= input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o número do quarto aluno: ")
Sorteio = [aluno1,aluno2,aluno3,aluno4]
print('O aluno escolhido para apagar o quadro foi: {}'.format(random.choice(Sorteio)))

