import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Função para buscar as taxas de câmbio
def buscar_taxas():
    url = "https://br.investing.com/currencies/exchange-rates-table"
    response = requests.get(url)
    html = BeautifulSoup(response.text, "html.parser")

    for dolar in html.select(".pid-2103-last"):
        MoedaTemp = dolar.text
        MoedaTemp = MoedaTemp.replace(",", ".")

    DolarReal = float(MoedaTemp)
    dolar_label.config(text=f"O dólar vale R${DolarReal:.2f}")

    for Eur in html.select(".pid-1617-last"):
        MoedaTemp = Eur.text
        MoedaTemp = MoedaTemp.replace(",", ".")

    EurReal = float(MoedaTemp)
    euro_label.config(text=f"O euro vale R${EurReal:.2f}")

# Função para converter uma quantidade específica para dólares e euros
def converter_moeda():
    quantidade_str = quantidade_entry.get()
    
    # Substituir ',' por '.'
    quantidade_str = quantidade_str.replace(',', '.')
    
    quantidade = float(quantidade_str)
    DolarReal = float(dolar_label.cget("text").split()[-1].replace("R$", "").replace(",", ""))
    EurReal = float(euro_label.cget("text").split()[-1].replace("R$", "").replace(",", ""))
    
    dolares_convertidos = quantidade / DolarReal
    euros_convertidos = quantidade / EurReal
    
    resultado_label.config(text=f"{quantidade:.2f} reais equivalem a:")
    resultado_dolar_label.config(text=f"{dolares_convertidos:.2f} dólares")
    resultado_euro_label.config(text=f"{euros_convertidos:.2f} euros")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Taxas de Câmbio")

# Alterar o esquema de cores da janela e dos widgets
janela.configure(bg='#87CEEB')  # Cor de fundo azul claro

# Botão para buscar as taxas
buscar_button = ttk.Button(janela, text="Buscar Taxas", command=buscar_taxas)
buscar_button.pack(pady=10)

# Rótulos para exibir as taxas de câmbio
dolar_label = ttk.Label(janela, text="", font=("Arial", 14), background='#87CEEB')  # Cor de fundo do rótulo
dolar_label.pack()
euro_label = ttk.Label(janela, text="", font=("Arial", 14), background='#87CEEB')  # Cor de fundo do rótulo
euro_label.pack()

# Entrada para a quantidade a ser convertida
quantidade_label = ttk.Label(janela, text="Digite a quantidade de reais:", font=("Arial", 12), background='#87CEEB')
quantidade_label.pack()
quantidade_entry = ttk.Entry(janela, font=("Arial", 12))
quantidade_entry.pack()

# Botão para converter
converter_button = ttk.Button(janela, text="Converter", command=converter_moeda)
converter_button.pack(pady=10)

# Rótulos para exibir o resultado da conversão
resultado_label = ttk.Label(janela, text="", font=("Arial", 12), background='#87CEEB')
resultado_label.pack()
resultado_dolar_label = ttk.Label(janela, text="", font=("Arial", 12), background='#87CEEB')
resultado_dolar_label.pack()
resultado_euro_label = ttk.Label(janela, text="", font=("Arial", 12), background='#87CEEB')
resultado_euro_label.pack()

# Loop principal da interface gráfica
janela.mainloop()
