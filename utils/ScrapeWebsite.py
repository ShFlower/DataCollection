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

    def sleep(self, sleeptime :int):
        time.sleep(sleeptime)

    #specify the xpath syntax given tagname,attribute and vlaue of web element or the specified list item    
    def find_tag_xpath(self, tagname :str, tag_attribute :str, tag_value :str, list_item :str, display_label :str):
             
        if len(list_item) > 0:
            node_xpath = (f"""//{tagname}[@{tag_attribute}="{tag_value}"]/{list_item}""")
        if len(display_label) > 0:
             node_xpath = (f"""//{tagname}[@{tag_attribute}="{tag_value}"]""")
        else:
             node_xpath = (f"""//{tagname}[@{tag_attribute}="{tag_value}"]""")
        return(node_xpath)
        time.sleep(2)

   
    def accept_element (self, user_selection_xpath :str):
        # find the xpath element first       
        accept_element_selection = self.driver.find_element(By.XPATH, user_selection_xpath)
        accept_element_selection.click()
        time.sleep(1)

    def find_filter_elements_using_span(self, tagname :str, attribute :str, value :str, filter_labels :list):
        #this does not differentiate between the must have and dont show lists which all get picked up together here
        filter_elements=[]  
        #in Main method call :bot.find_filter_elements_using_span(element_class = 'multiSelect-label', element_label = 'Garden')
        find_element_arg = '//'+tagname+'[contains(@' + attribute+',' + "'"+value + "'"+ ')]/span'
        #//div[contains(@class,'multiSelect-label']/span
        #print(find_element_arg)
        filter_elements = self.driver.find_elements(By.XPATH,find_element_arg) 
        for element in filter_elements:
            #print(element.text)
            if element.text in filter_labels:
                print(element.text)
                element.click()
        time.sleep(5)
    

    #works filter_elements = self.driver.find_elements(By.XPATH,"//div[contains(@data-test,'mustHave')]")
    #works filter_elements = self.driver.find_elements(By.XPATH, "//div[@data-test='garden-mustHave']")
    def find_filter_elements_using_contains(self, 
                                            tagname : str,
                                            element_attribute :str, 
                                            element_value :str,
                                            filter_elements_required :list):
        filter_elements=[]  
        find_element_arg = '//'+tagname+'[contains(@' + element_attribute+',' + "'"+element_value + "'"+ ')]'
        filter_elements = self.driver.find_elements(By.XPATH, find_element_arg)
        print(filter_elements)
        for element in filter_elements:
            print(element.text)
            if element.text in filter_elements_required :
                element.click()
        time.sleep(1)

    def accept_element_using_contains(self, 
                                    tagname : str,
                                    element_attribute :str, 
                                    element_value :str,
                                    required_value : str):
    
        find_element_arg = '//'+tagname+'[contains(@' + element_attribute+',' + "'"+element_value + "'"+ ')]'
        accept_element = self.driver.find_element(By.XPATH, find_element_arg)
        print(accept_element)
        if required_value.lower() == 'on' :
            accept_element.click()
        time.sleep(3)
        
        #Other tries that did not work
        #works filter_elements = self.driver.find_elements(By.XPATH, "//div[@data-test='garden-mustHave']")
        #filter_elements = self.driver.find_elements(By.cssSelector, "div[class='multiSelect-option multiSelect-option--selected'] [data-test='garden-mustHave']")
        #filter_elements.select_by_value(dropdown_selection) #Pass string argument 
        #filter_elements=self.driver.find_element(By.PARTIAL_LINK_TEXT, filter_labels)  
        
    
    def accept_element_by_name (self, element_value :str):
        # find the xpath element first       
        accept_element_selection = self.driver.find_element(By.NAME, element_value).click()
        time.sleep(1)

    def accept_element_containing_text(self, element_type :str, element_text :str, req_dropdown_element_index :int):
        found_elements=[]
        found_elements = self.driver.find_elements(By.XPATH, f"//{element_type}[text()='{element_text}']")
        print(f"found elements = {found_elements}")
        if isinstance(req_dropdown_element_index, int) :
            found_elements[req_dropdown_element_index].click()
        time.sleep(1)

    def check_for_fractions_in_string(self,dropdown_value :str):
        special_characters = "/"
        if any(c in special_characters for c in dropdown_value):
            char_position = dropdown_value.find("/")
            if (dropdown_value[char_position-1] == '1' and dropdown_value[char_position + 1] == '4'): 
                dropdown_value = str("Within "+ u"\u00bc" +" mile")
            if (dropdown_value[char_position-1] == '1' and dropdown_value[char_position + 1] == '2'): 
                dropdown_value = 'Within '+ u"\u00bd" +' mile'
            print(f"dropdown_unicode = {dropdown_value}") 
        return(dropdown_value)

    def set_dropdown_using_select_option(self, element_attribute :str, element_name :str, dropdown_string :str):
        #dropdown_element = self.driver.find_element (By.XPATH, ("//select[@name='radius']/option[text()='Within 20 miles']"))
        #dropdown_element = self.driver.find_element (By.XPATH, (f"//select[@name='radius']/option[text()='{dropdown_selection}']"))
        #works dropdown_element = self.driver.find_element (By.XPATH, (f"//select[@name='radius']/option[text()='{dropdown_value}']"))
        
        dropdown_string= self.check_for_fractions_in_string(dropdown_value = dropdown_string)
        
        find_element_arg = '(//select[@'+ element_attribute + '=' + "'" + element_name + "'"  + ']/option[text()=' + "'" + dropdown_string + "'" +'])'
        print(find_element_arg)
        dropdown_element = self.driver.find_element (By.XPATH,find_element_arg)
        dropdown_element.click()
        time.sleep(1)

    def set_dropdown_using_select_ByID(self, element_attribute :str, element_value :str, dropdown_selection :str):  
        selection=[] 
        selection = Select(self.driver.find_element(By.ID,element_value))
        print(selection)
        selection.select_by_value(dropdown_selection) #Pass string argument 
        time.sleep(1)

    def set_dropdown_using_select_ByNAME(self, element_value :str, dropdown_selection :str):  
        selection = Select(self.driver.find_element(By.NAME,element_value))
        selection.select_by_value(dropdown_selection) #Pass string argument 
        time.sleep(1)


    def set_dropdown_from_LoV_byID(self, element_value :str, dropdown_value :str):   
        index=0
        dropdown_list=[]
        dropdown_list = self.driver.find_element(By.XPATH, (f"//select[@id='{element_value}']")).find_elements(By.TAG_NAME, 'option')
        print(f"dropdown_list={dropdown_list}")
        for list_item in dropdown_list:
            print(list_item.get_attribute("value"))
            if list_item.get_attribute("value") == dropdown_value: 
                dropdown_list[index].click()
            index += 1
        time.sleep(2)           

           
  
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

   

   