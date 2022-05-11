def buscarCeps():
    #nao esta usando
    import html5lib
    import json
    import time
    import requests
    from bs4 import BeautifulSoup

    #esta usando
    import random
    import pandas as pd
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import numpy
    import lista

    #pega a lista do outro arquivo e declara a var lista
    lista = (lista.ListaDeCidade())
    #declara arr
    ceps = []
    #contador do loop
    contador = 0

    #loop percorre toda a lista e a cada cidade da lista busca o cep na url
    while contador < numpy.size(lista):
        
        aleatorio = random.uniform(0,1)
        temp = (round(aleatorio,1))
        #tempo para requests
        time.sleep(temp)
        #o contador e so para pegar da lista o item com a posição em que o contador esta
        url = "https://cep.guiamais.com.br/busca?word={}".format(lista[contador])

        #cada loope o contador adcina um
        contador+=1
        #printa o progresso
        print('buscando CEP : {}'.format(contador))

        #configuração para abri o navegador e buscar a url
        res = requests.get(url)
        #pegando html da pagina
        elemento = res.content


        #transformando em str
        elemento = str(elemento)

        print('<table class="table s_table_box table-striped table-responsive"> 'in elemento)


        #valida se esse tag com essa classe existe no HTML em que e feira a req
        #caso contrario significa que o cep nao foi encontrado.
        #nesse caso retornamos o valor de cep como 00000-000

        if ('<table class="table s_table_box table-striped table-responsive"> ' in elemento):
            #pega os dados da coluna 4 e passar para a coluna um (index)
            dados = pd.read_html(elemento, index_col=4)[0]
            #era pra pegar a cidade do cep , mas nem todos tinham, entao deixei pra pegar junto com o ibge
            #no caso na api do viacep
            city = pd.read_html(elemento, index_col=2)[0]

            #var recebe os dados da primeira coluna (index)
            cep = str(dados.index[0])
            print(cep)
            #adciona na ultima posição do arr o cep encontrado
            ceps.append(cep)

        else:
            #caso nao encontrar o cep retorna o cep como
            ceps.append('00000-000')

    return ceps

