#Exercício 02
#Uma empresa começou o dia com 320 unidade de mouses gamers no estoque. Durante o dia, foram vendidos 83 unidades e chegaram mais 112 de um fornecedor. Crie um programa que mostre o estoque inicial, a quantidade vendida, a reposição e o estoque ao final do dia.

Estoqueinc = int(input("Digite o estoque inicial"))
ProdutosVendidos = int(input("Digite a quantidade de mouses vendidos"))
Reposicao = int(input("Digite a quantidade de produtos qua chegaram para a reposição"))
Estoquefin = Estoqueinc - ProdutosVendidos + Reposicao

print(f"Com as vendas e asa reposições o estoque que era {Estoqueinc} agora é {Estoquefin}")