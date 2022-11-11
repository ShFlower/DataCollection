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