#A empresa Wilson Log tem uma rota de entrega. Essa rota inclui as seguintes cidades:
#São Paulo, Maringá, Curitiba, Joinvile e Caxias
#Uma empresa parceira adicionou  duas novas cidades: Londrina e Comboriú.
#Faça um código para: Unir as novas cidades na lista principal.
#indentificar a posição da cidade de Curitiba
#Inserir a cidade de pelótas na posição 4 e a cidade de Florianópolis na fim da lista.
#Remover a cidade que se encontra na posição 3
#Exibir uma mensagem final: "Maringá é a xª cidade da rota"

cidades = ["São Paulo", "Maringá", "Curitiba", "Joinvile", "Caxias"]
print(cidades)
cidades.append("Londrina")
print(cidades)
cidades.append("Camboriú")
posicao_curitiba = cidades.index("Curitiba")
print(posicao_curitiba)
cidades.insert(4, "Pelótas")
cidades.append("Floirianópolis")
print(cidades)
cidades.remove(3)
