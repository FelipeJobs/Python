#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
# usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas
# de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
from random import choice
sacar = int(input("Qual é o valor que você deseja sacar: "))
cedulas = [50,20,10,1]
quantidadedecedulas = []
saque =0
while True:
    cedula = choice(cedulas)
    saque = saque + cedula
    if saque > sacar:
        saque = saque - cedula
        cedula = 0
    quantidadedecedulas.append(cedula)
    if saque == sacar:
        break
print(f"""\33[34mO valor sacado foi repartido em:
{quantidadedecedulas.count(50)} cédulas de 50
{quantidadedecedulas.count(20)} cédulas de 20
{quantidadedecedulas.count(10)} cédulas de 10
{quantidadedecedulas.count(1)} cédulas de 1""")
print("----"*27)
print(f"\33[36mtotalizando: {sacar}")
print("----"*27)



