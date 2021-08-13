import matplotlib.pyplot as plt
import numpy as np

vendas = np.random.randint(1000, 3000, 50)
meses = np.arange(1, 51)

plt.figure(1, figsize=(15, 3))# tenho que colocar o tamanho da figura para ficar melhor 15largura, 3 altura
plt.subplot(1, 3, 1)# 1 linha de grafico na figure, 3 colunas, indice 1 pq quero ele em primeiro lugar na sequencia
plt.plot(meses, vendas,'b^-')
plt.subplot(1, 3, 2) # 2º grafico
plt.bar(meses,vendas)
plt.subplot(1, 3, 3) # 3º grafico
plt.scatter(meses,vendas)
plt.show()

