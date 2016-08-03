from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

timeOutExceptionMessage = "Timeout while waiting for element with id: '"
noSuchElementMessage = "Could not find element with ID: ''"
exceptionMessage = "An error occurred! "

def WaitForElement(driver, elementID, seconds):
    elementFound = True
    try:
        WebDriverWait(driver, seconds).until(EC.presence_of_element_located((By.ID, elementID)))
    except TimeoutException:
        elementFound = False
        print timeOutMessage + elementID + "'""
    except Exception, ex:
        elementFound = False
        print exceptionMessage + str(ex)
    finally:
        return elementFound

def GetElementByID(driver, elementID):
    element = None
    try:
        element = driver.find_element_by_id(elementID)
    except NoSuchElementException:
        print noSuchElementMessage + elementID + "'"
        element = None
    except Exception, ex:
        element = None
        print exceptionMessage + str(ex)
    finally:
        return element