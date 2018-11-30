from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import FirefoxOptions
import requests
import time
import sys
import os

opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=opts)
#driver = webdriver.Firefox()
driver.get("http://www.bolsadesantiago.com/mercado/Paginas/Acciones.aspx")
# Genero la fecha y la hora para el archivo de ejecucion
fechaHoy = time.strftime("%d%m%Y")
horaMinuto = time.strftime('%H%M')

directorioCrea="/home/ismael/CodigosPython/ObtieneDataAccion/dat/"+fechaHoy

nombreArchivo = directorioCrea+"/"+"infoAccion_" + fechaHoy + "_" + horaMinuto + ".info"
if os.path.exists(directorioCrea) == False:
	os.mkdir(directorioCrea)
else:
	print("no creo nada basura")
try:
    # Le digo que espere hasta que el combo box de acciones sea clickeable
    # El sitio espera hasta que ese combo sea clickeable para setear solo las acciones chilenas
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "FiltroTipoSelectBoxIt")))

    # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    html = BeautifulSoup(driver.page_source, "html.parser")

    # Obtenemos todos los divs donde estan las entradas
    entradas = html.find('table', {'id': 'tablaAcciones'})

    filasAcciones = entradas.find_all('tr', {'class': 'odd'})
    print(nombreArchivo)
    f = open(nombreArchivo, 'w')

    for i, accion in enumerate(filasAcciones):
        nombreAccion = accion.find('a', class_=False, id=False).getText()

        # claseBaja = accion.find('span', {'class','baja'})
        # claseAlta =accion.find('span', {'class','alza'})
        # variacion = ''
        # Valido si las variaciones son positivas, negativas o nulas
        # if claseBaja is not None:
        #	variacion = claseBaja.getText()
        # elif claseAlta is not None:
        #	variacion = claseAlta.getText()
        #	else:
        #		variacion = "0.0"
        listaCaracteristicas = accion.find_all('td', {'class', 'data-currency'})
        # Concateno todas las demas columnas para armar el string de carga masiva de datos
        caractUnidas = "|"
        for i, carac in enumerate(listaCaracteristicas):
            caractUnidas = caractUnidas + carac.getText() + "|"

        f.write(nombreAccion + caractUnidas + "\n")
    # Obtengo las demas acciones (20)
    filasAcciones2 = entradas.find_all('tr', {'class': 'even'})
    for j, accion2 in enumerate(filasAcciones2):
        nombreAccion = accion2.find('a', class_=False, id=False).getText()

        claseBaja = accion2.find('span', {'class', 'baja'})
        claseAlta = accion2.find('span', {'class', 'alza'})
        variacion = ''
        if claseBaja is not None:
            variacion = claseBaja.getText()
        elif claseAlta is not None:
            variacion = claseAlta.getText()
        else:
            variacion = "0.0"
        listaCaracteristicas = accion2.find_all('td', {'class', 'data-currency'})

        caractUnidas = "|"
        for i, carac in enumerate(listaCaracteristicas):
            caractUnidas = caractUnidas + carac.getText() + "|"

        f.write(nombreAccion + caractUnidas + "\n")

    print(len(entradas.find_all('tr', {'class': 'odd'})) + len(entradas.find_all('tr', {'class': 'even'})))


finally:
    f.close()
    driver.close()
