from selenium.webdriver.common.by import By
from pages.BookStoreLoginPage import BookStoreLoginPage

class BookStoreLandingPage:

    LOGIN_BUTTON=(By.CSS_SELECTOR,"#login")
    USER_NAME=(By.CSS_SELECTOR,"#userName")
    PASSWORD=(By.CSS_SELECTOR,"#password")


    def __init__(self,driver) -> None:
        self.driver=driver

    def navigateToLoginPage(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return BookStoreLoginPage(self.driver)
        