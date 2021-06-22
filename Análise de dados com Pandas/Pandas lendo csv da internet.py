#Caso 1: csv direto no link
import pandas as pd

url = 'https://drive.google.com/uc?authuser=0&id=1UzlPy6CZQeAzDXhfc_2sHEyK_Jb50vJs&export=download'
cotacao_df = pd.read_csv(url)
display(cotacao_df)


#Caso 2: csv em uma requisição que precisa ser tratada
import pandas as pd
import requests
import io #biblioteca io transforma texto em arquivo

url = 'http://portalweb.cooxupe.com.br:8080/portal/precohistoricocafe_2.jsp;jsessionid=8932C810E19A1D67A083743317FF11A3?d-3496238-e=2&6578706f7274=1'
#estou armazenando na variavel o conteudo deste link
conteudo_url = requests.get(url).content
#transformar o texto num arquivo para pandas ler
arquivo = io.StringIO(conteudo_url.decode('latin1'))
cafe_df = pd.read_csv(arquivo, sep=r'\t', engine='python')
display(cafe_df)
