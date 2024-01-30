from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import time 

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com/")
time.sleep(20)

#dados com o contato e mensagem
mensagem = 'ooooooooppppppaaaaaaaa'
contatos = ['ESTUDO E TESTES']

#buscar contatos/grupos 


#selectable-text copyable-text iq0m558w g0rxnol2

def buscar_contato(contato): 
    campo_pesquisa = driver.find_element(By.XPATH ,'//div[contains(@class,"selectable-text copyable-text iq0m558w g0rxnol2")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements(By.XPATH ,'//div[contains(@class,"selectable-text copyable-text iq0m558w g0rxnol2")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)
    
    
for contato in contatos: 
    buscar_contato(contato)
    enviar_mensagem(mensagem)















