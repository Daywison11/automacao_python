#nao esta usando nesse arquivo
import time
import pandas as pd
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#esta usando
import requests
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
#selecionar página
cidades = book['cidades']

#criação da primeira linha
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
    #DECLARANDO DADOS A SER SALVO

    #verifica se a api do ibge retorna erro
    if erro == {'erro': True}:
        #se retornar erro mostra no terminal que nao encontro o ibge
        print('nao encontrado')
        #na tabela (exel) adciona um as colnao como nao encontrado, com o cep pesquisado
        cidades.append(['nao encontrado', 'nao encontrado', cep[cont], 'nao encontrado'])
        cont += 1
    else:
        #caso nao tenha erro pega as variavei do objeto retornado
        ibge = (res['ibge'])
        uf = (res['uf'])
        cepurl = (res['cep'])
        localidade = (res['localidade'])

        #vai adcionar um array com todos os dados de cada cep pesquisados
        planilha.append( localidade + ' ' + uf + ' CEP: ' + cepurl + " IBGE : " +  ibge)

        #print(localidade + s + uf + ' CEP: ' + cepurl + " IBGE : " +  ibge )
        # print no status de busca
        print('buscando IBGE: {}'.format(cont))

        #MONTANDO PLANILHA com os dados
        cidades.append([localidade,uf,cepurl,ibge])#cada  dado e uma coluna
        cont += 1

#print no arr com todas as planilhas
print(planilha)

#SALVANDO PLANILHA com nome e extensao
book.save('planilha200A400.xlsx')