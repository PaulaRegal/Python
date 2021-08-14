vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]
lista_vendas2019 = []
#for para percorrer a lista, mas como é lista de tuplas faço unpack
for produto, vendas2019, vendas2020 in vendas_produtos:
    lista_vendas2019.append([vendas2019, produto])
print(lista_vendas2019)
print()

#Fazendo por list comprehension
lista_vendas2019_2 = [vendas2019 for produto, vendas2019, vendas2020 in vendas_produtos]
#leitura: para cada produto, vendas2019, vendas2020 na lista vendas_produtos quero apenas as vendas2019 na nova lista
print(lista_vendas2019_2)

#E se eu quisesse descobrir o produto que mais vendeu em 2019?
lista_vendasprodutos2019_2 = [(vendas2019, produto) for produto, vendas2019, vendas2020 in vendas_produtos]
print(max(lista_vendasprodutos2019_2))
#coloco vendas2019 primeiro pq no max procura o maior de acordo com o primeiro item que esta no parenteses
