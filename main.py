import time
import pandas as pd
import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import numpy
import Cep
import openpyxl

#CONFIGURAÇÃO PARA CRIA A PLANILHA
#criando planilha Book
book  = openpyxl.Workbook()
#visualizando paginas existente
print(book.sheetnames)
#criar pagina
book.create_sheet('cidades')
#selecionar ágina
cidades = book['cidades']

cidades.append(['CIDADE','ESTADO','CEP','IBGE'])
#============================

#=========================
#BUSCA IBGE MAIS CEP
cep = Cep.buscarCeps()
print(cep)
planilha = []
cont = int(0)
arrsize = numpy.size(cep)
#==========================

while cont < arrsize:
    #BUSCA DE DADOS
    url = "https://viacep.com.br/ws/{}/json/".format(cep[cont])

    print(url)
    res = requests.get(url)
    res = res.json()
    erro = res
    print(erro)
    #DECLARANDO DADOS A SER SALVO

    if erro == {'erro': True}:
        print('nao encontrado')
        cidades.append(['nao encontrado', 'nao encontrado', cep[cont], 'nao encontrado'])
        cont += 1
    else:
        ibge = (res['ibge'])
        uf = (res['uf'])
        cepurl = (res['cep'])
        localidade = (res['localidade'])
        s = ' '
        planilha.append( localidade + s + uf + ' CEP: ' + cepurl + " IBGE : " +  ibge)
        #print(localidade + s + uf + ' CEP: ' + cepurl + " IBGE : " +  ibge )
        print('buscando IBGE: {}'.format(cont))

        #MONTANDO PLANILHA
        cidades.append([localidade,uf,cepurl,ibge])
        cont += 1


print(planilha)
#SALVANDO PLANILHA
book.save('testeErro.xlsx')