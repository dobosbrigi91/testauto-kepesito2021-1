## 4 Feladat: Műveletek karakterekkel

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from random import randint

driver = webdriver.Chrome()
driver.get('https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html')

chr_mezo = driver.find_element_by_id('chr')
op_mezo = driver.find_element_by_id('op')
num_mezo = driver.find_element_by_id('num')
tabla = driver.find_element_by_xpath('//div/div/p[3]').text
kalkulacio_button = driver.find_element_by_id('submit')
eredmeny = driver.find_element_by_id('result')

# * Helyesen betöltődik az applikáció:
#     * Megjelenik az ABCs műveleti tábla, pontosan ezzel a szöveggel:
#       * !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

muveleti_tabla = str('!"#$' + "%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~")
assert tabla == muveleti_tabla

# * Megjelenik egy érvényes művelet:
#     * `chr` megző egy a fenti ABCs műveleti táblából származó karaktert tartalmaz
#     * `op` mező vagy + vagy - karaktert tartlamaz
#     * `num` mező egy egész számot tartalamaz
assert chr_mezo.text in tabla
assert op_mezo == '+' or '-'
print(float(num_mezo.text))

# * Gombnyomásra helyesen végződik el a random művelet a fenti ABCs tábla alapján:
#     * A megjelenő `chr` mezőben lévő karaktert kikeresve a táblában
#     * Ha a `+` művelet jelenik meg akkor balra lépve ha a `-` akkor jobbra lépve
#     * A `num` mezőben megjelenő mennyiségű karaktert
#     * az `result` mező helyes karaktert fog mutatni