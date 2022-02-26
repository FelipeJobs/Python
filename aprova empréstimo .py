# escreva um programa para aprovar um emprestimo para a compra de uma casa.
#O programa vai perguntar o valor do seu salário, o valor da casa e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário, se não o emprestimo será negado.
salario = float(input("Digite o valor do seu salário: "))
casa = float(input("Digite o valor do imovel que deseja adquirir: "))
anos = int(input("Em quantos anos pretende pagar o imóvel: "))
meses = anos * 12
parcela = float(casa // meses)
if parcela <= (salario * 0.3):
    print("Seu empréstimo foi aprovado")
else:
    print("Seu empréstimo não foi aprovado")


