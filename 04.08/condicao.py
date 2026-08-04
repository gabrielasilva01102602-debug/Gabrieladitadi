#Exercício 01:
#Uma empresa decidiu dar um bônus de 15% sobre o faturamento total para a equipe de vendas. Crie um programa para calcular o valor do bônus e o faturamento final da empresa após subtrair esse bônus.
#Faturamento Inicial: 50.000
#Percentual de bônus: 0.15
#Ao mostrar o resultado, mostre apenas duas casas decimais

Fatura = float(input("Qual sua fatura inicial?"))
bônus = Fatura * 0.15
print(f"o bônus é {bônus:.2f}")
faturafin = faturainc - bônus
print(f"Com o seu bonus de 15 porcento a fatura final será{faturafin:.2f}")
