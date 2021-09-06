## 4 Feladat: Műveletek karakterekkel

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

try:
    options = Options()
    options.headless = False

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
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


    def test_tc1():
        muveleti_tabla = str(
            '!"#$' + "%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~")
        assert tabla == muveleti_tabla

    # * Megjelenik egy érvényes művelet:
    def test_tc2():
        #     * `chr` megző egy a fenti ABCs műveleti táblából származó karaktert tartalmaz
        assert chr_mezo.text in tabla
        #     * `op` mező vagy + vagy - karaktert tartlamaz
        assert op_mezo == '+' or '-'
        #     * `num` mező egy egész számot tartalamaz

    # * Gombnyomásra helyesen végződik el a random művelet a fenti ABCs tábla alapján:

    #     * A megjelenő `chr` mezőben lévő karaktert kikeresve a táblában
    #     * Ha a `+` művelet jelenik meg akkor balra lépve ha a `-` akkor jobbra lépve
    #     * A `num` mezőben megjelenő mennyiségű karaktert
    #     * az `result` mező helyes karaktert fog mutatni
    def test_tc3():
        kalkulacio_button.click()
finally:
    driver.close()
