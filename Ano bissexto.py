# faça um programa que leia um ano qualquer e diga se ele é bissexto.
# isleap retorna true se o ano for bissexto.
import calendar
ano = int(input("Digite o valor do ano que gostaria de saber se é bissexto: "))
bissexto = calendar.isleap(ano)
if bissexto == True:
    print("O ano digitado é bissexto")
else:
    print("O ano digitado não é bissexto")
