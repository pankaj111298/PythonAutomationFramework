import pytest
from selenium import webdriver
from utils.Utilites import Utils
from jproperties import Properties


@pytest.fixture
def readFiles():
    utilites=Utils()
    configs=Properties()  
    configuration={}
    try:  
        file=utilites.readFile("C:\\Users\\Piyush\\Testing\\Automation\\PythonAutomationFramework\\resources\\config.properties")
        configs.load(file)
        items=configs.items()
        for item in items:
            configuration[item[0]]=item[1].data
        file.close()
    except Exception:
         print("Some issue with the code in the readFiles")

    yield configuration

      

    

@pytest.fixture
def driver(readFiles):
    if readFiles.get("browserName") == "chrome" :
        browser=webdriver.Chrome()
    elif readFiles.get("browserName") == "edge":
       browser=webdriver.Edge()
    else:
        raise Exception("Please enter correct browserName")
    browser.get(readFiles.get("URL"))
    browser.maximize_window()
    yield browser
    browser.quit()


