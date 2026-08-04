#A empresa Pioli S.A resolveu dar um aumento de salário aos seus colaboradores. Você foi contrartado para criar um progarama que calculará esses reajustes segundo os seguintes critérios:
#Salários até R$1240,00 : aumento de 20%
#Salários entre 1240,01 até 2500,00: aumento de 15%
#Salários entre 2500,00 e 2300,00: aumento de 10%
#Salários a partir de de 3200,00,01: aumento de 5%
#Imprima na tela: o salário antes do aumento, o percentual aplicado, o valor do aumento e o novo salário.

Salário = float(input("Digite seu salário"))
percentual = 0.20
percentual2 = 0.15
percentual3 = 0.10
percentual4 = 0.05
NovoSalário = Salário * percentual + Salário
if Salário >= 1240.00:
   print(f"o seu aumento será de{percentual * Salário} e o novo salario será{NovoSalário}")
elif Salário >= 1240.01 and Salário <= 2500.00:
   print(f"o seu aumento será de{percentual2 * Salário}")
elif Salário >= 2500.01 and Salário <= 3200.00:
   print(f"o seu aumento será de{percentual3 * Salário}")
else:
   print(f"o seu aumento será de{percentual4 * Salário}")


