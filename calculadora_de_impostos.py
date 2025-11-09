# Calculadora de impostos

income = float(input("Entre com os rendimentos anuais: "))

if income < 85528:
    tax = income * 0.18 - 556.02
    if tax < 0:
        tax = 0
else:
    tax = 14839.02 + (income - 85528) * 0.32

tax = round(tax, 0)
print("A taxa é:", tax, "thalers")

# Ela deve aceitar um valor de ponto flutuante: a receita.
# Em seguida, ele deve imprimir o imposto calculado, arredondado para inteiro. 
# Há uma função chamada round() que fará o arredondamento para você - 
# você a encontrará no código do esqueleto no editor.
# Nota: esse país feliz nunca devolveu dinheiro para seus cidadãos. 
# Se o imposto calculado for menor que zero, 
# isso significaria apenas nenhum imposto (o imposto foi igual a zero). 
#Leve isso em consideração durante os cálculos.

# se a renda do cidadão não era superior a 85.528 talões, 
# o imposto era igual a 18% da renda, menos 556 taller e 2 centavos.
# (isso era o que eles chamavam de isenção de imposto)
# se a receita fosse superior a esse valor, o imposto seria igual a 14.839 talões e 2 centavos. 
# mais 32% do excedente em mais de 85.528 taller.
