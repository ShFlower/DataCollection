from  utils.ScrapeWebsite import ScrapeWebsite

if __name__ == '__main__':
    
    #On RightMove website
    bot = ScrapeWebsite(site_url = 'https://www.rightmove.co.uk/')

    # 1. find cookie button and click accept cookies
    cookies_xpath= bot.find_node_xpath(tagname = 'button', 
                                        attribute = 'class', 
                                        value = 'optanon-allow-all accept-cookies-button',
                                        list_item ='')
    print(cookies_xpath)                        
    bot.accept_element(cookies_xpath)
    
   
    # 2. enter the search location either - site acepts a location name or a postcode
    # 2a. get the search bar xpath
    location_searchbar_xpath = bot.find_node_xpath(tagname = 'input', 
                                                attribute = 'class', 
                                                value = 'ksc_inputText ksc_typeAheadInputField',
                                                list_item='')
    # 2b. get the location entry specified by user
    location_user_input = bot.get_user_input()
    print(f"Location_user_input = {location_user_input}")

    #2c. get the search bar xpath and enter the user location into search bar
    bot.accept_search_element(location_searchbar_xpath, location_user_input)
    
    #2d. the site returns a dynamic list of suggested location in a drop down - accept the first item on list
    location_suggested_list_xpath=bot.find_node_xpath(tagname = 'ul', 
                                                attribute = 'class', 
                                                value = 'ksc_resultsList',
                                                list_item = 'li[1]') #accepts the first item in the suggested list
    print(f"location suggested list xpath= {location_suggested_list_xpath}")
    bot.accept_element(location_suggested_list_xpath)

    #time.sleep(5000)

    # 3. Find FOR SALE button and click to display for sale properties
    forsale_xpath=bot.find_node_xpath (tagname = 'button', 
                                        attribute = 'class', 
                                        value = 'ksc_button large primary searchPanelControls',
                                        list_item = '')                 
    print(forsale_xpath)      
    bot.accept_element_containing_text(forsale_xpath, find_string = 'For Sale')
                           

