#Filtrar lista de clientes inadimplentes
#O objetivo é identificar quem são os clientes inadimplentes e enviar essa lista de clientes para o setor de cobrança poder fazer a cobrança dos clientes.
# Vamos criar uma lista com os clientes inadimplentes (apenas o CPF e o valor que eles estão devendo)
#A inadimplência nessa empresa é calculada da seguinte forma:
#Se o cliente tiver devendo há mais de 20 dias, ele é considerado inadimplente.
#As informações vêm no formato (cpf, valor_devido, qtde de dias)
clientes_devedores = [('462.286.561-65', 14405, 24), ('251.569.170-81', 16027, 1), ('297.681.579-21', 8177, 28),
                      ('790.223.154-40', 9585, 10), ('810.442.219-10', 18826, 29), ('419.210.299-79', 11421, 15),
                      ('908.507.760-43', 12445, 24), ('911.238.364-17', 1345, 4), ('131.115.339-28', 11625, 8),
                      ('204.169.467-27', 5364, 22), ('470.806.376-11', 932, 29), ('938.608.980-69', 13809, 19),
                      ('554.684.165-26', 11227, 2), ('119.225.846-34', 4475, 9), ('358.890.858-95', 13932, 20),
                      ('786.547.940-70', 17048, 25), ('468.487.741-94', 2902, 8), ('540.685.100-32', 5806, 21),
                      ('379.729.796-80', 7622, 24), ('980.173.363-94', 13167, 24), ('833.285.374-56', 19581, 24),
                      ('103.669.436-50', 17126, 4), ('386.836.124-46', 18825, 11), ('588.404.964-15', 1545, 30),
                      ('600.556.177-18', 1921, 7), ('670.346.230-99', 18079, 28), ('771.352.915-13', 16581, 23),
                      ('430.314.324-46', 13942, 24), ('629.507.759-51', 17951, 11), ('348.683.225-73', 12424, 10),
                      ('406.133.151-17', 5888, 30), ('310.985.894-64', 17316, 30), ('964.317.132-30', 18818, 30),
                      ('845.331.524-14', 14284, 13), ('781.995.738-18', 19369, 29), ('921.558.128-63', 3206, 27)]

clientes_inadimplentes = []
for cpf, valor, dias in clientes_devedores:
    if dias > 20:
        clientes_inadimplentes.append(cpf)

# List Comprehension:
clientes_inadimplentes_2 = [cpf for cpf, valor, dias in clientes_devedores if dias > 20]

print(clientes_inadimplentes)
print(clientes_inadimplentes_2)

# Para identificar se as listas estão com mesmo tamanho:
print(len(clientes_inadimplentes))
print(len(clientes_inadimplentes_2))
print(len(clientes_devedores))