def ListaDeCidade():

    import json
    import time
    import requests
    import pandas as pd
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import numpy
#Pegar conteudo HTML a partir da URL
    url = "file:///C:/Users/Daywison/Documents/automa%C3%A7%C3%A3o%20python/table.html"


    option = Options()
    option.headless = True
    driver = webdriver.Chrome("C:/Users/Daywison/Downloads/chromedriver.exe")

    driver.get(url)
    element = driver.page_source

    elemento = str(element)
    city = pd.read_html(elemento,index_col=3, skiprows=100)[0].head(100)

    cidade = city.index
    driver.quit()


    list = []
    cont = 0
    while cont < numpy.size(cidade):
        cit_est =  cidade[cont]
        list.append(cit_est)
        cont+=1


    return list




