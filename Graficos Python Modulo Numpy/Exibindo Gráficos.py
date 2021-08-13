# módulo Matplotlib.pyplot. Existem outros, como o Seaborn e o Plotly
# site para consulta: https://matplotlib.org/stable/tutorials/introductory/pyplot.html
vendas_meses = [1500, 1727, 1350, 999, 1050, 1027, 1022, 1500, 2000, 2362, 2100, 2762]
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

import matplotlib.pyplot as plt

plt.plot(meses, vendas_meses)
plt.ylabel('Vendas')
plt.xlabel('Meses')
plt.axis([0, 12, 0, max(vendas_meses)+500])
#axis significa eixo, vc tem que passar valores min e  max do eixo x, depois para o y
#coloquei mais 500 para ter uma distancia do valor max de y
plt.show()