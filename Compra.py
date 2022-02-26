#Desenvolva um programa que calcule o valor a ser pago pelo produto de acordo com a forma de pagamento.
# a vista, dinheiro ou cheque 10% de desconto
# a vista no cartão 5 por cento de desconto.
# até duas vezes no cartão preço normal e em 3x mais 20% de juros
preço = float(input("Digite o preço do produto R$ "))
pagamento = int(input("Escolha a forma de pagamento\n 1= A vista\n 2= a vista no cartão\n 3= parcelado em até 2x\n 4= parcelado em 3x ou mais\n a qual é a opção escolhida: "))
vista = 0.9
vistac = 0.95
parcela = 1.2
if pagamento == 1:
    print("O valor a ser pago é de:R$", preço * vista)
elif pagamento == 2:
    print("O valor a ser pago é de: R$",preço * vistac)
elif pagamento == 3:
    print("O valor a ser pago é de: R$", preço)
elif pagamento == 4:
    print("O valor a ser pago é de: R$",preço * parcela)
