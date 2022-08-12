from dataclasses import replace
import requests
from bs4 import BeautifulSoup

url = "https://br.investing.com/currencies/exchange-rates-table"
response = requests.get(url)
html = BeautifulSoup(response.text,"html.parser")

for dolar in html.select(".pid-2103-last"):
    MoedaTemp = dolar.text
    MoedaTemp=MoedaTemp.replace(",",".")

DolarReal= float(MoedaTemp)
print(f"o dolar vale R${DolarReal:.2f}")

for Eur in html.select(".pid-1617-last"):
    MoedaTemp= Eur.text
    MoedaTemp=MoedaTemp.replace(",",".")

EurReal=float(MoedaTemp)
print(f"o eur vale R${EurReal:.2f}")
