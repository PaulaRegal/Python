import matplotlib.pyplot as plt
#https://plotly.com/python/#basic-charts biblioteca para criar graficos

import numpy as np
#docs.scipy.org/doc/numpy-1.15.0/reference/routines.random.html

vendas = np.random.randint(1000, 3000, 50)
# .randint gerar 50 numeros inteiros aleatórios entre o min1000, max2999
print(vendas)
meses = np.arange(1, 51) # inclui o primeiro numero e exclui o ultimo
print(meses)

plt.plot(meses, vendas,'b^-') # 'b^-': azul triangulo traço       'ro:' bola vermelha
plt.axis([0, 50, 0, max(vendas)+200])
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.show()