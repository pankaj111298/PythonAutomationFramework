import pytest
from pages.BookStoreLandingPage import BookStoreLandingPage


def test_BookStoreLogin(readFiles,driver):
    landingPage=BookStoreLandingPage(driver)
    loginPage=landingPage.navigateToLoginPage()
    loginPage.enterLoginDetails(readFiles.get("userName"),readFiles.get("password"))


# def test_fileReading():
#     file=Utils().readFile("./resources/config.properties")
#     configs=Properties()
#     configs.load(file)
#     print(configs.get())
