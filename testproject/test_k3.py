## 3 Feladat: Alfanumerikus mező

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

try:
    options = Options()
    options.headless = False

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get('https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html')

    # függvény a kitöltésre:
    def find_and_send_keys(title):
        song_title = driver.find_element_by_id('title')

        song_title.clear()
        song_title.send_keys(title)

    # * Helyes kitöltés esete:
    #     * title: abcd1234
    #     * Nincs validációs hibazüzenet
    def test_tc1():
        find_and_send_keys('abcd1234')
        error_message = driver.find_element_by_xpath('/html/body/form/span').get_attribute('class')
        assert error_message == 'error'

    # * Illegális karakterek esete:
    #     * title: teszt233@
    #     * Only a-z and 0-9 characters allewed.
    def test_tc2():
        find_and_send_keys('teszt233@')
        error_message2 = driver.find_element_by_xpath('/html/body/form/span').text
        assert error_message2 == 'Only a-z and 0-9 characters allewed'

    # * Tul rövid bemenet esete:
    #     * title: abcd
    #     * Title should be at least 8 characters; you entered 4.
    def test_tc3():
        find_and_send_keys('abcd')
        error_message3 = driver.find_element_by_xpath('/html/body/form/span').text
        assert error_message3 == 'Title should be at least 8 characters; you entered 4.'
finally:
    driver.close()