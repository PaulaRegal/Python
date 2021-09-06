import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
region = dados['region']

print('Detalhes do IP externo\n')
print('IP: {4}\nRegião: {1}\nPais: {2}\nCidade: {3}\nOrg: {0}'.format(org, region, pais, cid, ip))
#{4} significa que o print ficará na quarta posição