from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(options=options, service=servico)

#passo1
navegador.get("http://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M")

#passo2
navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys("Lucas Oliveira")
navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys("f.nrirdesign@gmail.com")
navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[3]/div/input').send_keys("61998029243")
#passo3
navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/button').click()