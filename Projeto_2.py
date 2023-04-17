from selenium   import webdriver
from selenium.webdriver.chrome.service  import Service as ChromeService
from webdriver_manager.chrome   import ChromeDriverManager
from selenium.webdriver.chrome.options  import Options
from selenium.webdriver.common.by   import By
from time   import sleep
import random

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', 'window-size=800,800']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)

    return driver

def digitando_humanamente(text, element):
    for letra in text:
        element.send_keys(letra)
        sleep(random.randint(1, 5)/30)

email_usuario = input('Digite seu Email ou telefone de login do Facebook: ')
senha_usuario = input('Digite sua senha de acesso ao Facebook: ')
status = input('Digite a Publicação que deseja fazer: ')

driver = iniciar_driver()
driver.get('https://www.facebook.com/')
sleep(5)


campo_email = driver.find_element(
    By.ID, 'email')
sleep(2)
digitando_humanamente(email_usuario, campo_email)

campo_senha = driver.find_element(
    By.ID, 'pass')
sleep(3)
digitando_humanamente(senha_usuario, campo_senha)

botao_entrar = driver.find_element(
    By.XPATH, '//button[@name="login"]')
sleep(3)
botao_entrar.click()
sleep(30)

driver.execute_script(
    'window.scrollTo(0, 500);')
sleep(3)
janela_status = driver.find_element(
    By.XPATH, '//div[@class="x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou"]')
sleep(2)
janela_status.click()
sleep(8)
 
dentro_janela_status = driver.find_element(
    By.XPATH, '//div[@class="xzsf02u x1a2a7pz x1n2onr6 x14wi4xw x9f619 x1lliihq x5yr21d xh8yej3 notranslate"]')
sleep(3)
digitando_humanamente(status, dentro_janela_status)
sleep(2)

botao_publicar = driver.find_element(
    By.XPATH, '//div[@class="x9f619 x1n2onr6 x1ja2u2z x193iq5w xeuugli x6s0dn4 x78zum5 x2lah0s x1fbi1t2 xl8fo4v"]//span[@class="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen x1s688f xtk6v10"]')
sleep(1)
botao_publicar.click()

driver.close()