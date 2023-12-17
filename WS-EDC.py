from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Tribuna import Tribuna
import time

# Inicializa o driver do navegador (certifique-se de ter o driver adequado instalado)
# Exemplo usando o driver do Chrome (https://sites.google.com/chromium.org/driver/)
driver = webdriver.Chrome()

# URL da página que você deseja percorrer
url = 'https://emdefesadocomunismo.com.br/tag/tribuna-debates/'

# Abre a página no navegador
driver.get(url)

# Aguarda um curto período de tempo para garantir que a página tenha carregado
time.sleep(2)
fim = False

# Faz scroll até o final da página
while True:
    body = driver.find_element('tag name', 'body')
    body.send_keys(Keys.END)

    # Aguarda um curto período de tempo para permitir a rolagem e carregamento da página
    time.sleep(2)
    fimElemen = driver.find_elements(By.CLASS_NAME, 'gh-card-date')
    ultimoElemento = fimElemen[-1]
    print(ultimoElemento.get_attribute('datetime'))
    fim = ultimoElemento.get_attribute('datetime')
    
    # Verifica se chegou ao final da página (você pode ajustar esse valor conforme necessário)
    if fim == '2023-08-09':
        break
tribunas = []
# Aguarda novamente para permitir que a página termine de carregar, se necessário
time.sleep(2)
article_links = []
articles = driver.find_elements(By.TAG_NAME,'article')
for article in articles:
    links = article.find_elements(By.TAG_NAME,'a')
    for link in links:
        tLink = link.get_attribute('href')
        tTitle = link.find_element(By.CLASS_NAME, 'gh-card-title').text
        tDesc = link.find_element(By.CLASS_NAME, 'gh-card-excerpt').text
        tData = link.find_element(By.CLASS_NAME, 'gh-card-date').text
        tribuna = Tribuna(tTitle, tDesc, tLink, tData)
        tribunas.append(tribuna)

for tribuna in tribunas:
    print('Título: ', tribuna.titulo)
    print('Descrição: ', tribuna.descricao)
    print('Data de Publicação: ', tribuna.data)
    print('Link: ', tribuna.link)
    print('=================================')

print(len(tribunas))


# Fecha o navegador
#driver.quit()

