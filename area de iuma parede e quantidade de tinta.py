#Faça um programa que receba a altura e alargura de uma parede e calcule a sua área. ademais deve informa quantos litros de tinta serão necessários para pinta-la sabendo que 1 litro pinta 2m²
Altura= int(input("Por favor informe a altura da parede: "))
largura= int(input("Por favor informe a largura da parede: "))
area = Altura*largura
tinta = area/2
print("a área da parede é:",area,"e você precisa de:",tinta,'litro de tinta para pintá-la.')

