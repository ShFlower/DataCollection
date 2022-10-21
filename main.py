from  utils.ScrapeWebsite import ScrapeWebsite

if __name__ == '__main__':
    
    #On RightMove website
    bot = ScrapeWebsite(site_url = 'https://www.rightmove.co.uk/')

    #On Website page 1:

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
    
    #2d. the search bar returns a dynamic list of suggested location in a drop down 
    #     by default accept the first item on list, else leave the last method argument empty
    
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
    bot.accept_button_containing_text(forsale_xpath, element_text = 'For Sale')
                           
# On website page 2
    #4. Set the search radius for the location specified, default to 1/4 mile
    
    '''searchradius_xpath=bot.find_node_xpath (tagname = 'div', 
                                        attribute = 'class', 
                                        value = 'touchsearch-selectwrapper touchsearch-searchcriteria-selectwrapper',
                                        list_item = '')
    print(forsale_xpath)'''
    #works bot.accept_form_containing_dropdown(searchradius_xpath, dropdown_selection = '') #no arg
    #works bot.accept_form_containing_dropdown(searchradius_xpath, dropdown_selection = "Within 20 miles") #whole number arg 
    #fracstr = 'Within '+ str(Fraction(1,4)) + ' miles'
    #print(fracstr)
    #bot.accept_form_containing_dropdown(searchradius_xpath, dropdown_selection = fracstr)  #fraction arg       
    #bot.accept_form_containing_dropdown_using_select(searchradius_xpath, dropdown_selection = "Within 1/4 miles")  
    #bot.accept_form_containing_dropdown_using_select(searchradius_xpath, dropdown_selection = "0.25") 
    #bot.accept_form_containing_dropdown_byValue(searchradius_xpath, dropdown_value = 0.25) 
    bot.accept_form_containing_dropdown_byValue(element_id = 'radius',dropdown_value = 0.25) 
    time.sleep(3)