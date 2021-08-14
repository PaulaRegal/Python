meta = 1000
vendas_produtos = [1500, 150, 2100, 1950]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']

#Fazendo por For tradicional:

produtos_acima_meta = []
# coloco o enumerate pq vou precisar do indice do produto para localizar na lista vendas_produtos
for i, produto in enumerate(produtos):
    if vendas_produtos[i] > meta:
        produtos_acima_meta.append(produto)
print(produtos_acima_meta)


#Fazendo por list comprehension:

produtos_acima_meta = [produto for i, produto in enumerate(produtos) if vendas_produtos[i] > meta]
print(produtos_acima_meta)