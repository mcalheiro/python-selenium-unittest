from selenium.webdriver.common.by import By


class MainPageLocators:

    GO_BUTTON = (By.ID, 'submit')


class SearchResultsPageLocators:

    RESULTS = (By.XPATH, '//h3[text()="Results"]')
