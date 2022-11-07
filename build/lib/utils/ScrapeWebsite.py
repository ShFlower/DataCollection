from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import nltk
import pandas as pd
#from typing import KeysView
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from fractions import *
from selenium.common.exceptions import NoSuchElementException


#custom methods or libraries
from utils.infinite_scroll import scroll_website

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

    #specify the xpath syntax given tagname,attribute and vlaue of web element
    # if using this method to deine a list item, then enter the list_item number e.g li[1]
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

    def select_element_from_list_of_elements (self, list_of_elements :str, select_criteria :list):
        for element in list_of_elements:
            #print(element.text)
            if element.text in select_criteria:
                print(element.text)
                element.click()
        time.sleep(5)

    def find_list_of_elements_using_span(self, tagname :str, attribute :str, value :str):
        #this does not differentiate between the must have and dont show lists which all get picked up together here
        list_of_elements=[]  
        #in Main method call :bot.find_filter_elements_using_span(element_class = 'multiSelect-label', element_label = 'Garden')
        find_element_arg = '//'+tagname+'[contains(@' + attribute+',' + "'"+value + "'"+ ')]/span'
        #//div[contains(@class,'multiSelect-label']/span
        print(find_element_arg)
        list_of_elements = self.driver.find_elements(By.XPATH,find_element_arg) 
        return(list_of_elements)

    def accept_element_using_span(self, tagname :str, attribute :str, value :str):
        find_element_arg = '//'+tagname+'[contains(@' + attribute+',' + "'"+value + "'"+ ')]/span'
        print(find_element_arg)
        next_button=self.driver.find_elements(By.XPATH,find_element_arg) 
        print(next_button)   


    def test_if_element_containing_textstring_exists(self, tagname :str, element_attribute :str, element_name :str, text_string :str):
        #find_element_arg = '(//select[@'+ element_attribute + '=' + "'" + element_name + "'"  + ']/option[text()=' + "'" + text_string + "'" +'])'
        #print(find_element_arg)

        #test_element=self.driver.find_element (By.XPATH,"//select[@class='pagination-button pagination-direction pagination-direction--next']/option[text()=' disabled']")
        pagination_button = self.find_tag_xpath(tagname='button', 
                                tag_attribute='title', 
                                tag_value='Next page', 
                                list_item='', 
                                display_label='')
        pagination_button2 = pagination_button + '/span'
        print(pagination_button2)

        #Attempt 1 : pagination_button = //button[@title="Next page"]/span  
        #Attempt 2 : pagination_button = //button[@title="Next page"] 
        try: 
            element_found=self.driver.find_element(By.XPATH,pagination_button)
            text_found= self.driver.find_element(By.XPATH, pagination_button2)
            print(element_found.text)
            if element_found.is_enabled:
                element_found.click()
                return(True)
            else:
                return(False)
        except NoSuchElementException: 
           print('No elements found')
           return(False)


    def scroll_results_pages(self, tagname :str, element_attribute :str, element_name :str, control_label :str):
        
        pagination_button = self.find_tag_xpath(tagname=tagname, 
                                tag_attribute=element_attribute, 
                                tag_value=element_name, 
                                list_item='', 
                                display_label='')
        #print(pagination_button)
        active_page_controls=[]
        try:
            active_page_controls = self.driver.find_elements(By.XPATH, pagination_button)
            if(len(active_page_controls) == 1 and active_page_controls[0].text != control_label):
                    return(False) 
            else:
                for page_control in active_page_controls:
                    print(f"page_control = {page_control.text}")
                    if page_control.text == control_label:
                        page_control.click()
                        return(True)
             
        except NoSuchElementException: 
            print('No elements found')
            
           
 
    def find_elements_in_search_listing(self, 
                                        search_container_xpath :str, 
                                        search_container_child_tag : str,
                                        page_control_tagname :str, 
                                        page_control_element_attribute :str, 
                                        page_control_element_name :str, 
                                        page_control_label :str):
        search_results=[]
        property_details=[]
        not_last_page = True
        property_search_results = self.driver.find_element(By.XPATH, search_container_xpath)
        #print(property_search_results.text)
        while (not_last_page == True):

            #scroll to bottom of search page
            scroll_website(self)

            # add all elements on the page to search element list
            search_results = property_search_results.find_elements(By.XPATH, search_container_child_tag) 
            print(len(search_results))
            link_content=[]
            for result in search_results: 
                #print(f" result = {result.text}") 
                try: 
                    #link = result.find_element(By.XPATH, './div/a').get_attribute('id')
                    link = result.find_element(By.XPATH, './div')
                    #link_content=link.text.split()
                    #link_content = nltk.word_tokenize(link.text)
                    print(f"link = {link.text}")
                    for item in link_content:
                        print(item.text)
                    property_details.append(link)

                except NoSuchElementException:
                    print(f"Did not find element : result is {link}")
                
            #check for multiple search pages and pagination controls to collate all search results
            not_last_page = self.scroll_results_pages(tagname = page_control_tagname, 
                                                                element_attribute = page_control_element_attribute, 
                                                                element_name = page_control_element_name, 
                                                                control_label =page_control_label)
        print(f"No of search elements = {len(property_details)}")
        print(*property_details)
           
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
        # find the xpath of an element using the element name.      
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

   

   