# Drag and Drop

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep


# ActionChain
from selenium.webdriver import ActionChains

class DragAndDrop:


   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       self.action = ActionChains(self.driver)


   def boot(self):
       self.driver.get(self.url)
       self.driver.maximize_window()
       sleep(5)


   def quit(self):
       self.driver.quit()


   def findElementById(self, id):
       return self.driver.find_element(by=By.ID, value=id)


   def dragAndDrop(self):
       try:
           self.boot()
           # we have to use 'switch_to.frame(0)' to to access the elements inside the iframe.
           self.driver.switch_to.frame(0)
           source = self.findElementById("draggable")
           destination = self.findElementById("droppable")
           # To perform the drage and drop
           self.action.drag_and_drop(source, destination).perform()
           sleep(3)


    
       except NoSuchElementException as e:
           print(e)
       finally:
           sleep(5)
           self.quit()




url = "https://jqueryui.com/droppable/"
obj = DragAndDrop(url)
obj.dragAndDrop()
