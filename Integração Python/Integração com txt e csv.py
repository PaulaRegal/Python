#1. Método open: -> Abre um arquivo txt
arquivo = open('NomeArquivo.txt', 'r')

#Usamos 'r' para abrir o arquivo para ler (read) e 'w' quando estamos abrindo o arquivo para
# escrever (write) ou 'a' se formos adicionar (append) uma informação no arquivo

#2. Método read():

texto_arquivo = arquivo.read()

#3. Método readlines():

lista_linhas = arquivo.readlines()

#4. Método write():

arquivo.write('Texto que quero escrever')

#Obs: Quando você abre um arquivo, ele permanece aberto no Python até você fechar.
# Existem 2 formas de fazer isso:
#1. Método close():

novo_arquivo = open('Resumo.txt', 'w') #abrir o txt
novo_arquivo_arquivo.write('Olá, meu nome é Paula.')
novo_arquivo.close() #tenho que fechar o arquivo para as edições realizadas serem aplicadas


#2. Usando a estrutura with: -> ao final do with, a própria estrutura with fecha automaticamente o arquivo

with open('Resumo2.txt', 'w') as arquivo2:
    arquivo2.write('Olá, seja bem vindo!')
    arquivo2.write('Espero contribuir com você!')

print('Fim do código')