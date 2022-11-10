from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def find_tag_xpath(self, tagname :str, tag_attribute :str, tag_value :str, list_item :str, display_label :str):
             
        if len(list_item) > 0:
            node_xpath = (f"""//{tagname}[@{tag_attribute}="{tag_value}"]/{list_item}""")
        if len(display_label) > 0:
             node_xpath = (f"""//{tagname}[@{tag_attribute}="{tag_value}"]""")
        else:
             node_xpath = (f"""//{tagname}[@{tag_attribute}="{tag_value}"]""")
        return(node_xpath)
        time.sleep(2)

def find_tag_xpath_using_contains(self, 
                                tagname : str,
                                tag_attribute :str, 
                                tag_value :str,
                                required_value : str):

    find_element_arg = '//'+tagname+'[contains(@' + tag_attribute+',' + "'"+tag_value + "'"+ ')]'
    found_element = self.driver.find_element(By.XPATH, find_element_arg)
    print(found_element)