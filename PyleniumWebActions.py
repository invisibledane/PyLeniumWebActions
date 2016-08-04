from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class Pylenium:
    def __init__(self):
        self.timeOutExceptionMessage = "Timeout while waiting for element with "
        self.noSuchElementMessage = "Could not find element with "
        self.exceptionMessage = "An error occurred! "
    
    # Find wait for an element and return it if found, can search by:
    # id, class, linktext (this text specifically)
    def WaitForElement(driver, elementID, seconds, type):
        element = None
        try:
            if type.lower() == 'id':
                element = WebDriverWait(driver, seconds).until(EC.presence_of_element_located((By.ID, elementID)))
            elif type.lower() == 'class'
                element = WebDriverWait(driver, seconds).until(EC.presence_of_element_located((By.CLASS_NAME, elementID)))
            elif type.lower() == 'linktext'
                element = WebDriverWait(driver, seconds).until(EC.presence_of_element_located((By.LINK_TEXT, elementID)))
        except TimeoutException:
            element = None
            print self.timeOutMessage + elementID + "'""
        except Exception, ex:
            element = None
            print self.exceptionMessage + str(ex)
        finally:
            return element

    def GetElementByID(driver, elementID):
        element = None
        try:
            element = driver.find_element_by_id(elementID)
        except NoSuchElementException:
            print self.noSuchElementMessage + "ID: '" + elementID + "'"
            element = None
        except Exception, ex:
            element = None
            print self.exceptionMessage + str(ex)
        finally:
            return element
    
    def GetElementByLinkText(driver, linkText):
        try:
            element = driver.find_element_by_link_text(linkText)
        except NoSuchElementException:
            print self.noSuchElementMessage + elementID + "'"
            element = None
        except Exception, ex:
            element = None
            print self.exceptionMessage + str(ex)
        finally:
            return element
    
    def GetElementByClassName(driver, className):
        try:
            element = driver.find_element_by_class_name(className)
        except NoSuchElementException:
            print self.noSuchElementMessage + elementID + "'"
            element = None
        except Exception, ex:
            element = None
            print self.exceptionMessage + str(ex)
        finally:
            return element
    
    def ClickItem(element):
        try:
            element.click()
            time.sleep(1)
        except Exception, ex:
            print self.exceptionMessage + str(ex)
    
    def GetText(element):
        itemText
        try:
            itemText = element.GetText()
        except Exception, ex:
            itemText = None
            print self.exceptionMessage + str(ex)
        finally:
            return itemText
    
    def SendKeyEnter(element):
        success = True
        try:
            element.send_keys(Keys.ENTER)
        except Exception, ex:
            success = False
            print self.exceptionMessage + str(ex)
        finally:
            return success
    
    def SendKeySpacebar(element):
        success = True
        try:
            element.send_keys(Keys.SPACE)
        except Exception, ex:
            success = False
            print self.exceptionMessage + str(ex)
        finally:
            return success
   
    def SendKeyTab(element):
        success = True
        try:
            element.send_keys(Keys.TAB)
        except Exception, ex:
            success = False
            print self.exceptionMessage + str(ex)
        finally:
            return success

    def SendKeyUpArrow(element):
        success = True
        try:
            element.send_keys(Keys.ARROW_UP)
        except Exception, ex:
            success = False
            print self.exceptionMessage + str(ex)
        finally:
            return success

    def SendKeyDownArrow(element):
        success = True
        try:
            element.send_keys(Keys.ARROW_DOWN)
        except Exception, ex:
            success = False
            print self.exceptionMessage + str(ex)
        finally:
            return success
    
    def SendKeyLeftnArrow(element):
        success = True
        try:
            element.send_keys(Keys.ARROW_LEFT)
        except Exception, ex:
            success = False
            print self.exceptionMessage + str(ex)
        finally:
            return success
    
    def SendKeyRightArrow(element):
        success = True
        try:
            element.send_keys(Keys.ARROW_RIGHT)
        except Exception, ex:
            success = False
            print self.exceptionMessage + str(ex)
        finally:
            return success
       
    def GoToURL(driver, URL):
        success = True
        try:
            driver.get(URL)
            time.sleep(2)
            if driver.current_url != URL:
                success = False
        except Exception, ex:
            success = False
            print self.exceptionMessage + str(ex)
        finally:
            return success

    def SendText(element, text):
        success = True
        try:
            element.clear()
            time.sleep(1)
            element.send_keys
        except Exception, ex:
            success = False
            print self.exceptionMessage + str(ex)
        finally:
            return success