# 🕸️ Web Scraping de Links com Requests e BeautifulSoup

Este script realiza uma extração de links (atributo `href` dos elementos `<a>`) de uma página web e grava os resultados em um arquivo CSV.

---

## 🚀 Funcionalidades

- Envia uma requisição HTTP para a URL: `https://wantedind.com/`
- Processa o HTML da página com BeautifulSoup
- Extrai os links (atributo `href`) de todos os elementos `<a>`
- Grava os links extraídos em um arquivo CSV chamado `data.csv`

---

## 🛠️ Bibliotecas Utilizadas

- **requests**: para enviar requisições HTTP e obter o conteúdo da página.
- **BeautifulSoup (bs4)**: para fazer o parsing do HTML e extrair informações.
- **csv**: para gravar os dados extraídos em um arquivo CSV.

---

## ▶️ Como Executar

1. **Instale as dependências**:

   ```bash
   pip install requests beautifulsoup4
   ```

2. **Salve o script** em um arquivo, por exemplo, `scraper.py`.

3. **Execute o script**:

   ```bash
   python scraper.py
   ```

4. Após a execução, um arquivo `data.csv` será gerado na mesma pasta, contendo os links extraídos.

---

## 📄 Código Completo

```python
import requests
from bs4 import BeautifulSoup
import csv

# Envia uma requisição HTTP para a página desejada
response = requests.get('https://wantedind.com/')

# Faz o parsing do HTML da página
soup = BeautifulSoup(response.text, 'html.parser')

# Abre o arquivo CSV para escrita e cria o objeto writer
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Link'])

    # Itera por todos os elementos <a> e extrai o atributo 'href'
    for link in soup.find_all('a'):
        data1 = link.get('href')
        writer.writerow([data1])
```

---

## ⚠️ Observações

- Verifique se a URL está acessível e se o scraping está de acordo com os termos de uso do site.
- Caso a estrutura do HTML mude, pode ser necessário ajustar a lógica de extração dos links.

---

## 📄 Licença

Este projeto é livre para uso e aprendizado. Use de forma ética e responsável.
