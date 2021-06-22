#criar uma tabela apenas com as vendas da Loja 306 e que não tiveram nenhuma devolução. 
#Quero criar essa tabela e saber quantas vendas são. Nesse caso são 2 condições.

#tudo junto --- parenteses para isolar as condições:
df_loja306semdevol = vendas_df[(vendas_df['ID Loja'] == 306) & (vendas_df['Quantidade Devolvida'] == 0)]
display(df_loja306semdevol)

#separado, primeiro crio minhas listas de comparações:
loja306 = vendas_df['ID Loja'] == 306
qtde_devolvida_0 = vendas_df['Quantidade Devolvida'] == 0
df2_loja306semdevolucao = vendas_df[loja306 & qtde_devolvida_0]
display(df2_loja306semdevolucao)