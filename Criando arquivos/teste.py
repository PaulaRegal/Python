#Criando um arquivo:
#escrever usa o 'w', se for atualizar usa o 'a'
def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    print(aluno_nota)

if __name__ == '__main__':
    #escrever_arquivo('Primeira linha. \n')
    aluno = '\nCesar, 7, 9, 3, 8'
    atualizar_arquivo('notas.txt', aluno)
    #ler_arquivo('teste.txt')