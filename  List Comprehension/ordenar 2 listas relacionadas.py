#Ordenar listas relacionadas:
vendas_produtos = [1500, 150, 2100, 1950]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']

# lista_aux é uma lista de tuplas, coloco list p/ transformar zip em lista
lista_aux = list(zip(vendas_produtos, produtos))

#ordenar do maior p/ menor. Coloquei vendas_produtos primeiro na lista pq a busca no sort será pelo 1º item
lista_aux.sort(reverse=True)
print(lista_aux)


#List Comprehension
#depois da lista ordenada faço um unpack, onde vendas é o 1º item da lista_aux e produto o 2º.
produtos = [produto for vendas, produto in lista_aux]
#como ler a linha de cod acima: para cada vendas e produtos da minha lista_aux, a minha lista de produtos será o produto
print(produtos)