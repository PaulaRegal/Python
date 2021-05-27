preco_produtos = [100, 150, 300, 5500]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']

# impostos é uma lista onde cada item é o preço * 30%, para cada preco dentro da lista preco_produtos  
impostos = [preco * 0.3 for preco in preco_produtos]
print(impostos)