from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

servico = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(options=options, service=servico)

#####
# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")

######wait 10 secs
input("Aperte enter após scanear o qr")

# Find the search bar and search for the desired contact
driver.find_element('xpath','//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').click()
driver.find_element('xpath','//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').send_keys("teste")
driver.find_element('xpath','//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').send_keys(Keys.RETURN)

# Wait for the search results to load
driver.implicitly_wait(4)

# Find the chat box and send the message
driver.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys("Ola, essa é uma mensagem automatica.")
driver.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.RETURN)

