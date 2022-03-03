#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo
# por extenso.
numero = 'Zero',"Um","Dois", "Três", "Quatro", "Cinco","Seis","Sete", "Oito","Nove","Dez","Onze","Doze",'Treze',"Quatorze","Quinze", "Dezesseis",'Dezessete','Dezoito','Dezenove','Vinte'
while True:
    digite = int(input("\33[34mDigite um número: "))
    if digite > 20:
        print("\33[31mvocê digitou um número inválido, tente novamente")
    if digite <= 20:
        print(f"\33[36mVocê digitou o número {numero[digite]}")
        break
print("Obrigado por utilizar o nosso programa, tenha um bom dia!!!")

