#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e
# fechados na ordem correta.
expressao = input('Digite uma expressão matemática: ')
paren = []
cont = 0
contd = 0

if '(' in expressao:
    paren.append('(')
    cont= cont+1
if ')' in expressao:
    paren.append(')')
    contd = contd +1
if cont == contd:
    print('\33[34mA sua expressão está escrita corretamente')
else:
    print('\33[31mA sua expressão está incorreta tente novamente.')