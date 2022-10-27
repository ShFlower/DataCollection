from  utils.ScrapeWebsite import ScrapeWebsite

if __name__ == '__main__':
    #On RightMove website
    bot = ScrapeWebsite(site_url = 'https://www.rightmove.co.uk/')

    #On Website page 1:
    # 1a. find cookie button and click accept cookies
    cookies_xpath= bot.find_tag_xpath(tagname = 'button', 
                                        tag_attribute = 'class', 
                                        tag_value = 'optanon-allow-all accept-cookies-button',
                                        list_item ='',
                                        display_label='')
    print(cookies_xpath)                        
    bot.accept_element(cookies_xpath)
    
   
    # 1b. enter the search location either - site acepts a location name or a postcode
    # 1b. get the search bar xpath
    location_searchbar_xpath = bot.find_tag_xpath(tagname = 'input', 
                                                tag_attribute = 'class', 
                                                tag_value = 'ksc_inputText ksc_typeAheadInputField',
                                                list_item='',
                                                display_label='')
    
    # 1c. get the location entry specified by user
    location_user_input = bot.get_user_input()
    print(f"Location_user_input = {location_user_input}")

    #1d. get the search bar xpath and enter the user location into search bar
    bot.accept_search_element(location_searchbar_xpath, location_user_input)
    
    #1e. the search bar returns a dynamic list of suggested location in a drop down 
    #     by default accept the first item on list, else leave the last method argument empty
    
    location_suggested_list_xpath=bot.find_tag_xpath(tagname = 'ul', 
                                                tag_attribute = 'class', 
                                                tag_value = 'ksc_resultsList',
                                                list_item = 'li[1]',
                                                display_label='') #accepts the first item in the suggested list
    print(f"location suggested list xpath= {location_suggested_list_xpath}")
    bot.accept_element(location_suggested_list_xpath)

    #time.sleep(5000)

    # 1f. Find FOR SALE button and click to display for sale properties
    forsale_xpath=bot.find_tag_xpath (tagname = 'button', 
                                        tag_attribute = 'class', 
                                        tag_value = 'ksc_button large primary searchPanelControls',
                                        list_item = '',
                                        display_label='')                 
    print(forsale_xpath)     
    bot.accept_element_containing_text(element_type='button', element_text = 'For Sale', req_dropdown_element_index = 0) 
                           
# On website page 2 
# https://www.rightmove.co.uk/property-for-sale/search.html?searchLocation=NW%20(Postcode%20Area)&useLocationIdentifier=true&locationIdentifier=REGION%5E93961&buy=For+sale
    
    #2a. Set the search radius for the location specified  
    bot.set_dropdown_using_select_ByID(element_attribute='By.ID', element_value='radius', dropdown_selection='0.25')
    #works bot.set_dropdown_from_LoV(element_id = 'radius',dropdown_value = '0.25')
    

    #2b. Set the min price for the properties searched   
    bot.set_dropdown_from_LoV(element_id = 'minPrice',dropdown_value = '50000') 

    #2c. Set the max price for the properties searched   
    bot.set_dropdown_from_LoV(element_id = 'maxPrice',dropdown_value = '1000000')  
    
    #2d. Set the min bedrooms for the properties searched   
    bot.set_dropdown_from_LoV(element_id = 'minBedrooms',dropdown_value = '1')  

    #2e. Set the max bedrooms for the properties searched   
    bot.set_dropdown_from_LoV(element_id = 'maxBedrooms',dropdown_value = '3')  

    #2f. Set the max bedrooms for the properties searched   
    bot.set_dropdown_from_LoV(element_id = 'displayPropertyType',dropdown_value = 'houses')

    #2g. Set the max bedrooms for the properties searched   
    bot.set_dropdown_from_LoV(element_id = 'maxDaysSinceAdded',dropdown_value = '7') 
    
    #2h. Select the find property button
    findproperty_xpath= bot.find_tag_xpath(tagname = 'button', 
                                        tag_attribute = 'class', 
                                        tag_value = 'button touchsearch-button touchsearch-primarybutton',
                                        list_item ='',
                                        display_label='')
                      
    bot.accept_element(findproperty_xpath)
    
# On website property listings page - Website page 3
# rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=REGION%5E93961&insId=1&radius=0.25&minPrice=50000&maxPrice=1000000&minBedrooms=1&maxBedrooms=3&displayPropertyType=houses&maxDaysSinceAdded=7&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false
    #bot3 = ScrapeWebsite(site_url = 'https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=REGION%5E93961&insId=1&radius=0.25&minPrice=50000&maxPrice=1000000&minBedrooms=1&maxBedrooms=3&displayPropertyType=houses&maxDaysSinceAdded=7&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false')
    #3a. select the filter option on the right of the black secondary menu bar along the top of page  
    filter_xpath = bot.find_tag_xpath(tagname = 'div', 
                                    tag_attribute = 'class', 
                                    tag_value = 'filtersBar-moreText',
                                    list_item ='',
                                    display_label='')
    bot.accept_element(filter_xpath)

    #3b. On filter dropdown page set the filter options
    #Filter Must Have options: Garden,Parking,New Home,Retirement Home,Buying Schemes,Auction Property
    #Filter Dont Show options: New Home,Retirement Home,Buying Schemes

    bot.find_filter_elements_using_contains(tagname='div',
                                            element_attribute='data-test',
                                            element_value  = 'mustHave',
                                            filter_elements_required = ['Garden','Parking'])  

    bot.find_filter_elements_using_contains(tagname='div',
                                            element_attribute='data-test',
                                            element_value  = 'dontShow',
                                            filter_elements_required = ['Retirement Home','Buying Schemes'])  

    #3c. Select the DONE button on the bottom right hand corner of page                                      
    done_xpath = bot.find_tag_xpath(tagname = 'button', 
                                    tag_attribute = 'data-test', 
                                    tag_value = 'apply-filters-button',
                                    list_item ='',
                                    display_label='')
    print(done_xpath)
    bot.accept_element(done_xpath)