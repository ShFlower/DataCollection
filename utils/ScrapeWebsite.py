from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
#from typing import KeysView
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from fractions import *


#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.action_chains import ActionChains

class ScrapeWebsite:

    def __init__(self, site_url :str):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
        #implicit wait
        #self.driver.implicitly_wait(0.5)
        #maximize browser

        self.driver.maximize_window()
        #driver get url
        self.driver.get(site_url)
        time.sleep(2)

    #specify the xpath syntax given tagname,attribute and vlaue of web element or the specified list item    
    def find_node_xpath(self, tagname :str, attribute :str, value :str, list_item :str, display_label :str):
             
        if len(list_item) > 0:
            node_xpath = (f"""//{tagname}[@{attribute}="{value}"]/{list_item}""")
        if len(display_label) > 0:
             node_xpath = (f"""//{tagname}[@{attribute}="{value}"]""")
        else:
             node_xpath = (f"""//{tagname}[@{attribute}="{value}"]""")
        return(node_xpath)
        time.sleep(2)

   
    def accept_element (self, user_selection_xpath :str):
        # find the xpath element first       
        accept_element_selection = self.driver.find_element(By.XPATH, user_selection_xpath)
        accept_element_selection.click()
        time.sleep(1)

    def accept_element_by_name (self, user_selection_xpath :str):
        # find the xpath element first       
        accept_element_selection = self.driver.find_element(By.XPATH, user_selection_xpath)
        accept_element_selection.click()
        time.sleep(1)

    def accept_button_containing_text(self, element_with_text_xpath :str, element_text :str):
        found_elements=[]
        found_elements = self.driver.find_elements(By.XPATH, f"//button[text()='{element_text}']")
        #print(f"found elements = {found_elements}")
        found_elements[0].click()
        time.sleep(1)

    def accept_form_containing_dropdown_frac(self, element_id :str, dropdown_value :str):
        #dropdown_element = self.driver.find_element (By.XPATH, ("//select[@name='radius']/option[text()='Within 20 miles']"))
        #dropdown_element = self.driver.find_element (By.XPATH, (f"//select[@name='radius']/option[text()='{dropdown_selection}']"))
        special_characters = "/"
        if any(c in special_characters for c in dropdown_value):
            char_position = dropdown_value.find("/")
            if (dropdown_value[char_position-1] == '1' and dropdown_value[char_position + 1] == '4'): 
                dropdown_value = str("Within "+ u"\u00bc" +" mile")
            if (dropdown_value[char_position-1] == '1' and dropdown_value[char_position + 1] == '2'): 
                dropdown_value = 'Within '+ u"\u00bd" +' mile'
            print(f"dropdown_unicode = {dropdown_value}")
        dropdown_element = self.driver.find_element (By.XPATH, (f"//select[@name='radius']/option[text()='{dropdown_value}']"))
        dropdown_element.click()
        time.sleep(15)

    def accept_form_containing_dropdown_using_select(self, element_with_dropdown_xpath :str, dropdown_selection :str):  
        selection=[] 
        selection = Select(self.driver.find_element(By.ID,'radius'))
        print(f"selection = {selection}")
        selection.select_by_value(dropdown_selection) #Pass integer 
        time.sleep(1)

    def accept_form_containing_dropdown(self, element_id :str, dropdown_value :str):   
        index=0
        dropdown_list=[]
        dropdown_list = self.driver.find_element(By.XPATH, (f"//select[@id='{element_id}']")).find_elements(By.TAG_NAME, 'option')
        for list_item in dropdown_list:
            if list_item.get_attribute("value") == dropdown_value: 
                dropdown_list[index].click()
            index += 1
        time.sleep(1)           

  
    def get_user_input(self):
        valid_input_flag = 0
        while valid_input_flag == 0:
            user_search_input = 'NW1 4NP'
            #valid_input_flag = self.validate_user_input(usr_search_input)
            valid_input_flag =1 #remove this line once method validate_user_input has been constructed
        return(user_search_input)

    def accept_search_element(self, search_element_xpath :str, user_input :str):
        # find the xpath element first       
        accept_search_selection = self.driver.find_element(By.XPATH, search_element_xpath)
        accept_search_selection.click()
        
        # then send the string to be entered into the search bar
        accept_search_selection.send_keys(user_input)
        time.sleep(2)

   

   