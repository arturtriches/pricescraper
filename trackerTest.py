import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import json
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.5"
}

def abrir_tabela():
    with open("config.json", 'r', encoding='utf-8') as arq:
       return json.load(arq)

def olhar_preco(URL):
    pagina = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(pagina.content, "html.parser")
    try:
        preco = soup.find("span",{"class":"a-price aok-align-center reinventPricePriceToPayMargin priceToPay apex-pricetopay-value"})
        if preco:
            return preco.text
    except AttributeError:
        return "Deu erro!"

def printar():
    cfg = abrir_tabela()
    
    for p in cfg["Itens"]:
        nome = p["nome"]
        url = p["url"]
        print(f"Item: {nome}, {olhar_preco(url)}")
        
printar()
        