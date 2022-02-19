def buscarCeps():
    #nao esta usando
    import html5lib
    import json
    import time
    import requests
    from bs4 import BeautifulSoup

    #esta usando
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

        #o contador e so para pegar da lista o item com a posição em que o contador esta
        url = "https://cep.guiamais.com.br/busca?word={}".format(lista[contador])

        #cada loope o contador adcina um
        contador+=1
        #printa o progresso
        print('buscando CEP : {}'.format(contador))

        #configuração para abri o navegador e buscar a url
        option = Options()
        option.headless = True

        #essa rota muda conforma a maquina que esta o arquivo do drive
        driver = webdriver.Chrome("C:/Users/Daywison/Downloads/chromedriver.exe")

        #buscando a url
        driver.get(url)

        #pegando html da pagina
        element = driver.page_source

        #transformando em str
        elemento = str(element)
        #fechando navegador
        driver.quit()

        print('<table class="table s_table_box table-striped table-responsive"> 'in elemento)

        #essa validadação foi a que te falei que nao funciona muito bem, mas dexei mesmo assim
        #era pra validar se uma tabela com 4 coluna  no html

        if ('<table class="table s_table_box table-striped table-responsive"> ' in elemento):
            #pega os dados da coluna 4 e passar para a coluna um
            dados = pd.read_html(elemento, index_col=4)[0]

            #era pra pegar a cidade do cep , mas nem todos tinham, entao deixei pra pegar junto com o ibge
            city = pd.read_html(elemento, index_col=2)[0]

            #var recebe os dados da primeira coluna (index)
            cep = str(dados.index[0])

            #adciona na ultima posição do arr o cep encontrado
            ceps.append(cep)

        else:
            #caso nao encontrasse era pra retornar esse cep
            # so que nao funciona
            ceps.append('00000-000')

    return ceps

buscarCeps()