## 5 Feladat: Bingo

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

try:
    options = Options()
    options.headless = False

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get('https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html')

    cellak = driver.find_elements_by_xpath('//tbody//td')
    szamok = driver.find_elements_by_xpath('//ol/li')

    # * Az applikáció helyesen megjelenik:
    def test_tc1():
        # * A bingo tábla 25 darab cellát tartalmaz
        assert len(cellak) == 25
        # * A számlista 75 számot tartalmaz
        assert len(szamok) == 75


    # * Bingo számok ellenőzrzése:


    def test_tc2():
        play_button = driver.find_element_by_id('spin')
        # * Addig nyomjuk a `play` gobot amíg az első bingo felirat meg nem jelenik
        for play in range(75):
            message = driver.find_element_by_xpath('//ul[@id="messages"]').text
            if message == 'BINGO':
                break
            else:
                play_button.click()
        # szelvény számai:
        eltalalt_tabla = driver.find_elements_by_xpath('//td[@class="checked"]')
        talalt = []
        for szam in eltalalt_tabla:
            talalt.append(szam.text)
        # jelölt számok:
        eltalalt_szam = driver.find_elements_by_xpath('//li[@class="checked"]/input')
        jelolt_szam = []
        for szam in eltalalt_szam:
            jelolt_szam.append(szam.get_attribute('value'))
        # Ellenőrizzük, hogy a bingo sorában vagy oszlopában lévő számok a szelvényről tényleg a már kihúzott
        # számok közül kerültek-e ki:
        for talalt in jelolt_szam:
            assert talalt in jelolt_szam

    # * Új játékot tudunk indítani
    def test_tc3():
        # előző számok
        bingo_szamok = []
        for cella in cellak:
            bingo_szamok.append(cella.text)
        # * az init gomb megnyomásával a felület visszatér a kiindulási értékekhez
        # kattintás a init gombra:
        driver.find_element_by_id('init').click()
        # * új bingo szelvényt kapunk más számokkal.
        uj_cellak = driver.find_elements_by_xpath('//tbody//td')
        uj_szamok = []
        for cella in uj_cellak:
            uj_szamok.append(cella.text)
        assert bingo_szamok is not uj_szamok
finally:
    driver.close()