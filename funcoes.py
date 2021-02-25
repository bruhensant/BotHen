import urllib.request
from random import randint

def rolar(f):
    return randint(1,f)

def dado(d): # 2dx
    v = []
    c = 0
    d = d.split('d') # d = ['x','x']
    l = [int(x) for x in d] # d = [x,x]

    while c < l[0]:
        c += 1
        v.append(rolar(l[1]))

    t = sum(v)

    return v, t

def convert_usd(valor):

    valor = valor.replace(',','.')

    link = urllib.request.urlopen('https://economia.awesomeapi.com.br/USD-BRL') # link da cotação
    html = link.read() # lê o link
    textosite = str(html) # transforma conteúdo em txt

    listachaves = list(textosite.split(',')) # lista com as chaves

    chave = listachaves.pop(8) # corta a chave na gambiarra

    dividido = list(chave.split('"')) # divide a chave gambiarruda

    ask = float(dividido.pop(3)) # retira o valor de dentro da chave dividida

    resultado = ask * float(valor)

    return resultado

def convert_ars(valor):

    valor = valor.replace(',','.')

    link = urllib.request.urlopen('https://economia.awesomeapi.com.br/ARS-BRL') # link da cotação
    html = link.read() # lê o link
    textosite = str(html) # transforma conteúdo em txt

    listachaves = list(textosite.split(',')) # lista com as chaves

    chave = listachaves.pop(8) # corta a chave na gambiarra

    dividido = list(chave.split('"')) # divide a chave gambiarruda

    ask = float(dividido.pop(3)) # retira o valor de dentro da chave dividida

    resultado = ask * float(valor)

    return resultado