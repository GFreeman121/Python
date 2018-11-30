from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup


browser=webdriver.Firefox()
browser.get('http://www.bolsadesantiago.com/mercado/Paginas/Acciones.aspx');
input=browser.find_element_by_id('FiltroNombre')
input.send_keys('CHILE')
btnBuscar=browser.find_element_by_id('buttonBuscarAccionDesfase')
btnBuscar.click()

#html que voy a parsear hermano
html=browser.page_source
print(html)

