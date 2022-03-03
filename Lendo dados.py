#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres
# têm menos de 20 anos.
idadem = []
nomem = []
sexom= []
nomef = []
sexof = []
idadef =[]
somam = 0
somaf = 0
menorque20 = 0
for c in range(1,5):
    nome = input("\33[32mQual é o nome da {}º pessoa: ".format(c))
    idade =int(input("\33[34mQual é a sua idade: "))
    sexo =input("\33[33mQual é o seu sexo: ")
    espaço = print("-=" * 13)
    if sexo == "F" or sexo == "f":
        nomef.append(nome)
        idadef.append(idade)
        sexof.append(sexo)
        somaf = float(idade + somaf)
    if sexo == "M" or sexo == "m":
        nomem.append(nome)
        idadem.append(idade)
        sexom.append(sexo)
        somam = float(idade+somam)
for c in idadef:
    if c < 20:
        menorque20 = menorque20 +1
print("\33[34mA idade média do grupo é: {}.".format((somam+somaf)//4))
print("\33[31mO homem mais velho tem",max(idadem),"anos","e se chama",nomem[idadem.index(max(idadem))])
print("\33[32mTemos {} mulheres com menos de 20 anos".format(menorque20))
