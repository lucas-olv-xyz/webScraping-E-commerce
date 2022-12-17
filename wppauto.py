from selenium import webdriver

# Replace 'contact_name' with the name of the contact you want to send the message to
contact_name = 'teste'

# Replace 'message_text' with the text of the message you want to send
message_text = 'Ola, essa é uma mensagem automatica.'

# Start a webdriver and open the WhatsApp web interface
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

# Wait for the page to load
driver.implicitly_wait(10)

# Find the search bar and search for the contact
driver.find_element('xpath','/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]')
driver.send_keys(contact_name)

# Wait for the search results to load
driver.implicitly_wait(4)

# Find the contact in the search results and click on it
driver.find_element('xpath','/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[8]/div/div/div/div[2]').click()

# Find the text input field and send the message
driver.find_element('xpath','/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(message_text)

# Find the send button and click on it
driver.find_element('xpath','/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()

