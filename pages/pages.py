from pages.elements import BasePageElement
from pages.locators import MainPageLocators, SearchResultsPageLocators


class SearchTextElement(BasePageElement):

    locator = 'q'


class BasePage:

    def __init__(self, driver) -> None:
        self.driver = driver


class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def is_in_page(self) -> bool:
        return 'Python' in self.driver.title
    
    def click_go_button(self) -> None:
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class SearchResultsPage(BasePage):

    def has_results(self) -> bool:
        return 'No results found.' not in self.driver.page_source
