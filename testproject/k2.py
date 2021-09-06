## 2 Feladat: Színes reakció

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
driver.get('https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html')

# lokátorok meghatározása
random_szin = driver.find_element_by_id('randomColorName').text
valtozo_szin = driver.find_element_by_id('testColorName').text
start_button = driver.find_element_by_id('start')
stop_button = driver.find_element_by_id('stop')
result = driver.find_element_by_id('result').text

# * Helyesen jelenik meg az applikáció betöltéskor:
#     * Alapból egy random kiválasztott szín jelenik meg az `==` bal oldalanán. A jobb oldalon csak a `[  ]` szimbólum
#     látszik.
#     <szín neve> [     ] == [     ]



#* El lehet indítani a játékot a `start` gommbal.
 #   * Ha elindult a játék akkor a `stop` gombbal le lehet állítani.


assert result == ''

start_button.click()
stop_button.click()

assert result == 'Incorrect!' or 'Correct!'


# * Eltaláltam, vagy nem találtam el.
#     * Ha leállítom a játékot két helyes működés van, ha akkor állítom épp le
#     amikor a bal és a jobb oldal ugyan azt a színt tartalmazza akkor a `Correct!` felirat jelenik meg.
#       ha akkor amikor eltérő szín van a jobb és bal oldalon akkor az `Incorrect!` felirat kell megjelenjen.

start_button.click()
time.sleep(5)
stop_button.click()
time.sleep(3)

if random_szin == valtozo_szin:
    assert result == 'Correct!'
else:
    assert result == 'Incorrect!'