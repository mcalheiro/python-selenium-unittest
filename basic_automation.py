import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class PythonOrgSearch(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
    
    def tearDown(self) -> None:
        self.driver.close()

    def test_search_in_python_org(self) -> None:
        driver = self.driver
        driver.get('https://www.python.org/')
        assert 'Python' in driver.title
        search_bar = driver.find_element(By.NAME, 'q')
        search_bar.clear()
        search_bar.send_keys('pycon')
        search_bar.send_keys(Keys.RETURN)
        assert 'No results fould.' not in driver.page_source

if __name__ == '__main__':
    unittest.main()
