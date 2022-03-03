# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e quantos dolares ela pode comprar com esse dinheiro.
Dinheiro =float(input("Quanto você tem na sua carteira? "))
Dolar = 3.27
if Dinheiro/Dolar == 1:
    print("Você pode comprar até",float(Dinheiro/Dolar),"Dolar.")
elif Dinheiro/Dolar >1:
    print("Você pode comprar até", float(Dinheiro / Dolar), "Dolares.")
elif (Dinheiro/Dolar <1):
    print("Você não tem dinheiro suficiente para adquirir essa moeda.")


