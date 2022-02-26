#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua idade as seguintes informações:
#Se ele ainda vai se alistar ao serviço militar
# se é hora de se alistar.
# se já passou do tempo de alistamento. além disso, o programa deve dizer quanto tempo falta para se alistar ou quanto tempo já passou do prazo.
#è assim que se importa o ano atual a sintase é dessa forma.
import datetime
data = datetime.date.today()
ano = int(data.strftime("%Y"))
nascimento = int(input("Digite o o seu ano de nascimento para verificarmos o alistamento militar: "))
minimo = 18
idade = ano - nascimento
if idade < minimo:
    print("Ainda não é necessário se alistar faltam {} anos.".format(minimo - idade))
    print("O ano que você deverá se alistar sera: {}".format(abs(minimo-idade + ano)))
elif idade == minimo:
    print("Esse é o ano para você se alistar")
else:
    print("Você deveria ter se aliastado a {} anos".format(idade - minimo))
    print("O ano do seu alistamento foi: {}".format(abs(idade - minimo - ano)))

