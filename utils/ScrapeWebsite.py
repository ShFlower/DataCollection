from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import nltk
import pandas as pd
import re
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

        self.property_info ={} #defines dictionary
        self.list_of_property_info=[] #defines list of dictionary

    def sleep(self, sleeptime :int):
        time.sleep(sleeptime)

    #specify the xpath syntax given tagname,attribute and vlaue of web element
    # if using this method to deine a list item, then enter the list_item number e.g li[1]
    def find_element_xpath(self, tagname :str, tag_attribute :str, tag_value :str, list_item :str, display_label :str):
          
        if len(list_item) > 0:
            node_xpath = (f"""//{tagname}[@{tag_attribute}="{tag_value}"]/{list_item}""")
        if len(display_label) > 0:
             node_xpath = (f"""//{tagname}[@{tag_attribute}="{tag_value}"]""")
        else:
             node_xpath = (f"""//{tagname}[@{tag_attribute}="{tag_value}"]""")
        return(node_xpath)
        time.sleep(2)

    def find_relative_element_xpath_using_contains(self, 
                                tagname : str,
                                tag_attribute :str, 
                                tag_value :str,
                                required_value : str):

        #find_element_arg = '//'+tagname+'[contains(@' + tag_attribute+',' + "'"+tag_value + "'"+ ')]'
        find_element_arg = (f"""//{tagname}[contains(@{tag_attribute},"{tag_value}")]""")
        #find_element_arg = '//'
        print(find_element_arg)
        try:
            found_element = self.driver.find_element(By.XPATH, find_element_arg)
            return(found_element)
        except NoSuchElementException: 
            print('No elements found')
        

    def find_absolute_element_xpath_using_contains(self, 
                                tagname : str,
                                tag_attribute :str, 
                                tag_value :str,
                                required_value : str):

        find_element_arg = '/'+tagname+'[contains(@' + tag_attribute+',' + "'"+tag_value + "'"+ ')]'
        return(find_element_arg)
        

    def find_list_of_elements_using_contains(self, 
                                            tagname : str,
                                            tag_attribute :str, 
                                            tag_value :str,
                                            required_value : str):

        find_element_arg = '/'+tagname+'[contains(@' + tag_attribute+',' + "'"+tag_value + "'"+ ')]'
        found_elements=[]
        try:
            found_elements = self.driver.find_elements(By.XPATH, find_element_arg)
        except NoSuchElementException: 
            print('No elements found')
        return(found_elements)

    def accept_element (self, user_selection_xpath :str):
        # find the xpath element first       
        accept_element_selection = self.driver.find_element(By.XPATH, user_selection_xpath)
        accept_element_selection.click()
        time.sleep(1)

    def select_element_from_list_of_elements (self, list_of_elements :str, dict_entry :list):
        for element in list_of_elements:
            #print(element.text)
            if element.text in select_criteria:
                print(element.text)
                element.click()
        time.sleep(5)
    
    def find_element_using_span(self, tagname :str, attribute :str, value :str):
        find_element_arg = '//'+tagname+'[contains(@' + attribute+',' + "'"+value + "'"+ ')]/span'
        print(find_element_arg)
        found_element = self.driver.find_elements(By.XPATH,find_element_arg) 
        return(found_element)


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


    def scroll_results_pages(self, tagname :str, element_attribute :str, element_name :str, control_label :str):
        
        pagination_button = self.find_element_xpath(tagname=tagname, 
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

    '''property_address_xpath = property.find_element(By.XPATH,find_relative_element_xpath_using_contains(tagname = 'h1',
                                                                                        tag_attribute ='itemprop', 
                                                                                        tag_value = 'streetAddress',
                                                                                        required_value =''))
            #print(property_address_xpath)'''        

    def extract_property_details(self, search_urls :list):

        for property_url in search_urls:
        
            self.driver.get(property_url)
            property_address=self.driver.find_element(By.XPATH,value='//h1[@itemprop="streetAddress"]').text
            print(property_address)
            property_country=self.driver.find_element(By.XPATH,'//meta[@itemprop="addressCountry"]').get_attribute('content')
            print(property_country)
            property_price_xpath = self.find_element_xpath(tagname ='button', 
                                                        tag_attribute = 'aria-label', 
                                                        tag_value ='Note on property price', 
                                                        list_item ='', 
                                                        display_label ='')
                             
            property_price = self.driver.find_element(By.XPATH,'//button[@aria-label="Note on property price"]//parent::span//parent::div/span').text
            print(property_price)
            property_added =  self.driver.find_element(By.XPATH,'//div[contains(text(),"Added on ")]').text 
            print(property_added)      
            #self.driver.quit()
            time.sleep(1)
      
    def find_items_in_search_listing(self, 
                                    search_container_xpath :str, 
                                    search_container_child_tag : str,
                                    page_control_tagname :str, 
                                    page_control_element_attribute :str, 
                                    page_control_element_name :str, 
                                    page_control_label :str):
        
        search_results=[] # all elements returned by search
        property_urls=[] # list of properties urls from serach listing
        #print(search_container_xpath) - //*[@id="l-searchResults"]/div
        #print(search_container_child_tag) - ./div
        
        not_last_page = True
        
        while (not_last_page == True):

            #scroll to bottom of search page
            scroll_website(self)
            property_list = self.driver.find_element(By.XPATH,'//div[@class="l-searchResults"]/div')
            #print(property_list.text)

            search_results = property_list.find_elements(By.XPATH, './div')
            print(len(search_results))
            #print(*search_results)
           

            for result in search_results:
                try: # to test for banners in the search for banners in the search list
                    result.find_element(By.XPATH,'./div/a')
                    property_id_label= result.find_element(By.XPATH,'./div/a').get_attribute('id')
                    print (property_id_label) 
                    try: # find the property url
                        property_url = result.find_element(By.XPATH, '//a[@data-test="property-camera-icon"]').get_attribute('href')
                        print(property_url)
                    except NoSuchElementException: 
                        property_url = result.find_element(By.XPATH, '//a[@data-test="property-img"]').get_attribute('href')
                        print(property_url)
                    #print(property_url)
                    property_urls.append(property_url)
                except NoSuchElementException:
                    print("Did not find element")  
        
               
            #check for multiple search pages and pagination controls to collate all search results
            not_last_page = self.scroll_results_pages(tagname = page_control_tagname, 
                                                                element_attribute = page_control_element_attribute, 
                                                                element_name = page_control_element_name, 
                                                                control_label =page_control_label)
        
        print(f"No of search elements = {len(property_urls)}")
        print(*property_urls)
        return(property_urls)

    def extract_property_info(self, search_list :list):
        print(f"No of properties = {len(search_list)}")
        for item in search_list:
            print(item)
            #item.click()
            #result_item = result.find_element(By.XPATH, './div/a').get_attribute('id')
            property_id_element = item.find_element(By.XPATH,'/div/a')
            property_id = property_id_element.get_attribute('id')
            print(property_id)
            property_info = {property_id: property_id}
            
            #except NoSuchElementException:
            #print('Did not find element')


        #property_ = extract_property_information(property_page=result_item)
        #list_of_property_info.append(property_info)  
        #print(*list_of_property_info)'''
            
        '''list_of_property_information.append(property_info)  '''

        #print(*list_of_property_info)
           
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
                                    tag_attribute :str, 
                                    tag_value :str,
                                    required_value : str):
    
        find_element_arg = '//'+tagname+'[contains(@' + tag_attribute+',' + "'"+tag_value + "'"+ ')]'
        found_element = self.driver.find_element(By.XPATH, find_element_arg)
        print(found_element)
        if required_value.lower() == 'on' :
            found_element.click()
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

   

   