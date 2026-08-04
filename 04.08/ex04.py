#Uma loja de produtos eletrônicos tem os seguintes produtos em estoque:
#monitor, teclado, mouse, headset
#O gerente te pediu pediu para adicionar webcam no final da lista 
# #Atualizar o teclado para teclado mecânico
#Verificar se tem impressora na lista 
# Remover o mouse da lista 

estoque = ["monitor", "teclado", "mouse", "headset"]
print(estoque)
estoque.append("webcam")
print(estoque)
posicao_teclado = estoque.index("teclado") 
print(posicao_teclado)
estoque[1] = "teclado mecânico"
print(estoque)
impressora_no_estoque ="impressora" in estoque
print("impressora no estoque?", impressora_no_estoque)
estoque.remove("mouse")
print(estoque)
estoque.insert(2, "mouse")
print(estoque)