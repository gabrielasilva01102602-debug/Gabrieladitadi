# print("Olá, Mundo!")
# nome = "Gabriela"
# idade = 15
# altura = 1.72

# print("Nome:", nome)
# print("idade", idade)
# print("Altura", altura)

# num1 = int(input("Digite o primeiro número"))
# num2 = int(input("Digite o segundo número"))
# soma = num1 + num2
# sub = num1 - num2
# multi = num1 * num2
# div = num1 / num2

# print("soma", soma)
# print("sub", sub)
# print("multi", multi)
# print("div", div)

#Criar variável salário e dividir esse  salário por 30. Em seguida fazer uma condicional para saber se o salário é baixo ou alto

salario = float(input("Meu salário")) 
div = salario / 30
print(f"salario diario {div:.2f}")

if salario > 2000:
    print("Você ganha bem")
else:
    print("Salário Minimo")
    