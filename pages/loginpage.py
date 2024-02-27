import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.visionplus.id'


    def open(self):
        self.driver.get(self.url)
        time.sleep(3)
    
    def clickLogin(self, username, password):
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//span[contains(text(), "Log in/Register")]').click()
        mainWindow = self.driver.current_window_handle  
        for handle in self.driver.window_handles:  
            if handle != mainWindow:
                self.driver.switch_to.window(handle)
                break
        time.sleep(1)
        title = self.driver.title
        print(title)
        self.driver.find_element(By.XPATH, "//input[@id='phone']").send_keys(username)
        self.driver.find_element(By.XPATH, "//input[@id='fld_Password']").send_keys(password)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@id='btn_Login']").click()
        time.sleep(5)
    
    def successLogin(self):
        # get window pertama, karena case diatas click login, dia nutup window, dan disini mesti get window lagi karena beda function
        mainWindow = self.driver.window_handles[0]  
        self.driver.switch_to.window(mainWindow)
        print(self.driver.title)
        success_element = self.driver.find_element(By.XPATH, "//div[contains(text(),'Hello!')]")
        return success_element

        
    def closeBrowser(self):
        if self.driver.session_id:
            self.driver.close()

    def wrongPassword(self):
        return self.driver.find_element(By.XPATH, "//h3[contains(text(),'Wrong phone number or password')]")

    def unregisteredAkun(self):
        return self.driver.find_element(By.XPATH, "//h3[contains(text(),'This account has not been registered.')]")
