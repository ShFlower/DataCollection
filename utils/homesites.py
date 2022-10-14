from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
#from typing import KeysView
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.rightmove.co.uk/")
time.sleep(5)

