def soma():
    a = int(input("Digite o valor de um número: "))
    soma = a
    while True:
        b = int(input("Digite o valor do número que acrescentar ao anterior: "))
        soma = soma + b
        print(f"A soma dos números é: {soma}")
        continuar = input("Você deseja continuar somando valores S/N: ").upper()
        if continuar == "N":
            break
#essa função vai somar novos valores até o usuário finalizar
soma()