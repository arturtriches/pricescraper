
import pandas as pd; import time; import random; import json
from selenium import webdriver
import selenium.webdriver.common.by
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=options)

def abrir_tabela():
    with open("config.json", 'r', encoding='utf-8') as arq:
       return json.load(arq)

def olhar_preco(URL):
    driver.get(URL)
    try:
        preco = driver.find_element(selenium.webdriver.common.by.By.CLASS_NAME, "a-price")
        if preco:
            return preco.text.replace("\n",",")
    except AttributeError:
        return "Deu erro!"

def printar():
    cfg = abrir_tabela()
    
    for p in cfg["Itens"]:
        nome = p["nome"]
        url = p["url"]
        print(f"Item: {nome}: {olhar_preco(url)}")
        
printar()
        