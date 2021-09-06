## 2 Feladat: Színes reakció

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
try:
    options = Options()
    options.headless = False

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get('https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html')

    # lokátorok meghatározása
    random_szin = driver.find_element_by_id('randomColorName')
    valtozo_szin = driver.find_element_by_id('testColorName')
    start_button = driver.find_element_by_id('start')
    stop_button = driver.find_element_by_id('stop')
    result = driver.find_element_by_id('result').text


    # * Helyesen jelenik meg az applikáció betöltéskor:
    #     * Alapból egy random kiválasztott szín jelenik meg az `==` bal oldalanán. A jobb oldalon csak a `[  ]` szimbólum
    #     látszik.
    #     <szín neve> [     ] == [     ]
    def test_tc1():
        latszik = random_szin.text + driver.find_element_by_id('randomColor').text + \
                  '==' + driver.find_element_by_id('testColor').text + valtozo_szin.text
        print(latszik)


    #  El lehet indítani a játékot a `start` gommbal.
    # * Ha elindult a játék akkor a `stop` gombbal le lehet állítani.
    def test_tc2():
        assert result == ''
        start_button.click()
        stop_button.click()
        assert result == 'Incorrect!' or 'Correct!'


    # * Eltaláltam, vagy nem találtam el.
    #     * Ha leállítom a játékot két helyes működés van, ha akkor állítom épp le
    #     amikor a bal és a jobb oldal ugyan azt a színt tartalmazza akkor a `Correct!` felirat jelenik meg.
    #       ha akkor amikor eltérő szín van a jobb és bal oldalon akkor az `Incorrect!` felirat kell megjelenjen.
    def test_tc3():
        start_button.click()
        time.sleep(5)
        stop_button.click()
        time.sleep(3)

        if random_szin.text == valtozo_szin.text:
            result2 = driver.find_element_by_id('result').text
            assert result2 == 'Correct!'
        else:
            result2 = driver.find_element_by_id('result').text
            assert result2 == 'Incorrect!'
finally:
    driver.close()