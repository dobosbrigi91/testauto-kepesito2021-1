## 1 Feladat: Pitagorasz-tétel

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

try:
    options = Options()
    options.headless = False

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get('https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html')

    # oldalak meghatározása id lokátorral:
    a_oldal = driver.find_element_by_id('a')
    b_oldal = driver.find_element_by_id('b')

    # függvény az adatok beírására és a kalkuláció gomb megnyomására:
    def calculate(a, b):
        a_oldal.clear()
        b_oldal.clear()

        a_oldal.send_keys(a)
        b_oldal.send_keys(b)

        driver.find_element_by_id('submit').click()


    # Helyesen jelenik meg az applikáció betöltéskor:
    # * a: <üres>
    # * b: <üres>
    # * c: <nem látszik>


    def test_tc1():
        assert a_oldal.text == ''
        assert b_oldal.text == ''
        result = driver.find_element_by_id('results').get_attribute('style')
        assert result == 'display: none;'

    # * Számítás helyes, megfelelő bemenettel
    #     * a: 2
    #     * b: 3
    #     * c: 10

    def test_tc2():
        test_data = [2, 3]
        calculate(test_data[0], test_data[1])
        c = int(driver.find_element_by_id('result').text)
        assert c == 10


    # * Üres kitöltés:
    #     * a: <üres>
    #     * b: <üres>
    #     * c: NaN


    def test_tc3():
        test_data2 = ['']
        calculate(test_data2[0], test_data2[0])
        c = int(driver.find_element_by_id('result').text)
        assert c == 'NaN'
finally:
    driver.close()
