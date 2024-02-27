from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.maximize_window()
    
driver.get("https://www.visionplus.id/webclient/#/")
driver.find_element(By.XPATH, '//span[contains(text(), "Log in/Register")]').click()
time.sleep(1)
mainWindow = driver.current_window_handle
time.sleep(2)
for handle in driver.window_handles:
    if handle != mainWindow:
        driver.switch_to.window(handle)
        break
webSkrg = driver.title
print(webSkrg)
driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("08997775838")
driver.find_element(By.XPATH, "//input[@id='fld_Password']").send_keys("4321lupa")

# driver.find_element(By.XPATH, "//input[@id='password']").send_keys("4321lupa")
time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='btn_Login']").click()
time.sleep(5)
windowutama = driver.window_handles[0]
driver.switch_to.window(windowutama)
driver.find_element(By.XPATH, "//div[contains(text(),'Hello!')]")
driver.find_element(By.XPATH, "//span[contains(text(), 'My profile')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[contains(text(), 'Live TV')]").click()
time.sleep(1)
wait = WebDriverWait(driver, 10)
time.sleep(10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='player']")))
hoverTV = driver.find_element(By.XPATH, "//video[@id = 'video']")
# atribut_hover = hoverTV.get_attribute('paused')
# title_h = hoverTV.get_attribute('title')
# print(atribut_hover)
# print(title_h)
try:
    # get selector element pause
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#player > div > div.player-paused.layout-align-center-center.layout-column")))
    print("element ada")
except:
    print("element tidak ada brarti belom dipause")
    actions = ActionChains(driver)
    actions.move_to_element(hoverTV).perform()
    time.sleep(2)
    hoverPause = driver.find_element(By.XPATH, "//button[@class= 'md-icon-button pause md-button md-ink-ripple']").click()
    # get selector element pause
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#player > div > div.player-paused.layout-align-center-center.layout-column")))
    print("element  ada, sudah kepause, dari variable hoverPause")


time.sleep(1000)

