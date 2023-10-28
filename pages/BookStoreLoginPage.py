from selenium.webdriver.common.by import By

class BookStoreLoginPage:
    LOGIN_BUTTON=(By.CSS_SELECTOR,"#login")
    USER_NAME=(By.CSS_SELECTOR,"#userName")
    PASSWORD=(By.CSS_SELECTOR,"#password")

    def __init__(self,driver) -> None:
        self.driver=driver

    def enterLoginDetails(self,userName,password):
        userNameField=self.driver.find_element(*self.USER_NAME)
        passwordField=self.driver.find_element(*self.PASSWORD)
        loginButtonField=self.driver.find_element(*self.LOGIN_BUTTON)
        userNameField.send_keys(userName)
        passwordField.send_keys(password)
        loginButtonField.click()
