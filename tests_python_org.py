import unittest
from selenium import webdriver
from pages import pages


class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.python.org/')

    def test_search_in_python_org(self):
        main_page = pages.MainPage(self.driver)
        self.assertTrue(main_page.is_in_page())
        main_page.search_text_element = 'pycon'
        main_page.click_go_button()
        search_results_page = pages.SearchResultsPage(self.driver)
        self.assertTrue(search_results_page.has_results())

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
