def buscarCeps():
    import html5lib
    import json
    import time
    import requests
    import pandas as pd
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import numpy
    import lista


    lista = (lista.ListaDeCidade())
    ceps = []
    contador = 0



    while contador < numpy.size(lista):

        url = "https://cep.guiamais.com.br/busca?word={}".format(lista[contador])
        contador+=1
        print('buscando CEP : {}'.format(contador))

        option = Options()
        option.headless = True
        driver = webdriver.Chrome("C:/Users/Daywison/Downloads/chromedriver.exe")

        driver.get(url)
        element = driver.page_source

        elemento = str(element)

        driver.quit()

        if (pd.read_html(elemento, index_col=4)):
            dados = pd.read_html(elemento, index_col=4)[0]

            city = pd.read_html(elemento, index_col=2)[0]

            cep = str(dados.index[0])
            ceps.append(cep)

        else:
            ceps.append('00000-000')

    return ceps