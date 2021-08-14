#As lambdas expressions são funções anônimas (sem nome mesmo) que tem 1 linha de código e são atribuidas a uma variável, como se a variável virasse uma função.
#Elas normalmente são usadas para fazer uma única ação, mas em Python usamos principalmente dentro de métodos como argumento, para não precisarmos criar uma função só para isso
#Outra aplicação delas está em criar um "gerador de funções"

#Estrutura:
# minha_funcao = lambda parametro: expressão
# #quando quer utilizar uma função que vai executar apenas uma linha de codigo
# parametro é o argumento que fica entre parenteses na função
# expressao é o que ela te da como resposta

#Definindo uma função e chamando:
def minha_funcao(num):
    return num * 2
print(minha_funcao(5))

#Lambda vc ja cria a função direto:
minha_funcao2 = lambda num: num * 2
print(minha_funcao2(5))

#Definindo uma função:
imposto = 0.3
def preco_imposto(preco):
    return preco * (1 + imposto)
print(preco_imposto(100))

#lambda expressions para criar uma função que calcula o preço dos produtos acrescido do imposto
preco_imposto2 = lambda preco: preco * (1.0 + imposto) # pode ser 0.3 ao inves de imposto
print(preco_imposto2(100))