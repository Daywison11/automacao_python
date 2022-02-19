def ListaDeCidade():
    #nao esta usando
    import json
    import requests
    from bs4 import BeautifulSoup

    #esta usando
    import time
    import pandas as pd
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import numpy
#Pegar conteudo HTML a partir da URL
    url = "file:///C:/Users/Daywison/Documents/automa%C3%A7%C3%A3o%20python/table.html"


    option = Options()
    option.headless = True
    driver = webdriver.Chrome("C:/Users/Daywison/Downloads/chromedriver.exe")

    driver.get(url)

    #pegando o html da pagina
    element = driver.page_source
    #transformando em uma string
    elemento = str(element)

    #trasformando o conteudo em uma tabela
    #os paramentros são:

    # o elemento a ser tratado, >>(elemento)<<
    # a coluna que eu quero que seja a primeira, no caso passa da 3 para a index, >>(index_col=)<<
    # e o numero de linhas a serem ignoradas. >>(skiprows=100)<<
    # e o numero maximo de linhas que eu quero >>(.head(numero))<<
    city = pd.read_html(elemento,index_col=3, skiprows=100)[0].head(5)

    # pegando a primeira coluna e armazenando em cidades
    cidade = city.index

    #para o codigo antes de passar para a linha de baixo (segundos)
    time.sleep(10)

    #fecha a pagina com a tabela
    driver.quit()

    #declarando array
    list = []

    #contador do loop
    cont = 0

    #loop vai percorrer a tabela e criar um novo array >>list<<
    while cont < numpy.size(cidade):
        cit_est =  cidade[cont]
        list.append(cit_est)
        cont+=1


    return list




