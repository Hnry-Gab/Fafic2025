servicos = [["name", "desc", "price", "horario"]]

# lista de serviços = lista dos valores do produto
nome = input()
horario = input()
for servico in servicos:
    if nome == servico[0] and horario == servico[3]:
        print("Já existe")





# servicos = []

# nome = input()
# desc = input()
# valor = input()
# horario = input()
# tipo = input() # servico/produto

# servicos.append([nome, desc, valor, horario])

# for servico in servicos:
#     if nome == servico[0]:
#         print("Já existe")