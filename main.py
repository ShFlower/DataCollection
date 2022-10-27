from  utils.ScrapeWebsite import ScrapeWebsite

if __name__ == '__main__':
    
 '''   #On RightMove website
    bot = ScrapeWebsite(site_url = 'https://www.rightmove.co.uk/')

    #On Website page 1:

    # 1. find cookie button and click accept cookies
    cookies_xpath= bot.find_node_xpath(tagname = 'button', 
                                        attribute = 'class', 
                                        value = 'optanon-allow-all accept-cookies-button',
                                        list_item ='',
                                        display_label='')
    print(cookies_xpath)                        
    bot.accept_element(cookies_xpath)
    
   
    # 2. enter the search location either - site acepts a location name or a postcode
    # 2a. get the search bar xpath
    location_searchbar_xpath = bot.find_node_xpath(tagname = 'input', 
                                                attribute = 'class', 
                                                value = 'ksc_inputText ksc_typeAheadInputField',
                                                list_item='',
                                                display_label='')
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
                                                list_item = 'li[1]',
                                                display_label='') #accepts the first item in the suggested list
    print(f"location suggested list xpath= {location_suggested_list_xpath}")
    bot.accept_element(location_suggested_list_xpath)

    #time.sleep(5000)

    # 3. Find FOR SALE button and click to display for sale properties
    forsale_xpath=bot.find_node_xpath (tagname = 'button', 
                                        attribute = 'class', 
                                        value = 'ksc_button large primary searchPanelControls',
                                        list_item = '',
                                        display_label='')                 
    print(forsale_xpath)     
    bot.accept_element_containing_text(element_type='button', element_text = 'For Sale', req_dropdown_element_index = 0) 
                           
# On website page 2 
# https://www.rightmove.co.uk/property-for-sale/search.html?searchLocation=NW%20(Postcode%20Area)&useLocationIdentifier=true&locationIdentifier=REGION%5E93961&buy=For+sale
    
    #4a. Set the search radius for the location specified  
    bot.set_dropdown_using_select_ByID(element_attribute='By.ID', element_label='radius', dropdown_selection='0.25')
    #bot.set_dropdown_using_unicode_for_fraction(element_id = 'radius', dropdown_value = 'Within 1/2 mile')
    #bot.set_dropdown_from_LoV(element_id = 'radius',dropdown_value = '0.25')
    

    #4b. Set the min price for the properties searched   
    bot.set_dropdown_from_LoV(element_id = 'minPrice',dropdown_value = '50000') 

    #4c. Set the max price for the properties searched   
    bot.set_dropdown_from_LoV(element_id = 'maxPrice',dropdown_value = '1000000')  
    
    #4d. Set the min bedrooms for the properties searched   
    bot.set_dropdown_from_LoV(element_id = 'minBedrooms',dropdown_value = '1')  

    #4e. Set the max bedrooms for the properties searched   
    bot.set_dropdown_from_LoV(element_id = 'maxBedrooms',dropdown_value = '3')  

    #4f. Set the max bedrooms for the properties searched   
    bot.set_dropdown_from_LoV(element_id = 'displayPropertyType',dropdown_value = 'houses')

    #4g. Set the max bedrooms for the properties searched   
    bot.set_dropdown_from_LoV(element_id = 'maxDaysSinceAdded',dropdown_value = '7') 
    
    #4h. Select the find property button
    findproperty_xpath= bot.find_node_xpath(tagname = 'button', 
                                        attribute = 'class', 
                                        value = 'button touchsearch-button touchsearch-primarybutton',
                                        list_item ='',
                                        display_label='')
                      
    bot.accept_element(findproperty_xpath)'''
    
# On website property listings page - Website page 3
# rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=REGION%5E93961&insId=1&radius=0.25&minPrice=50000&maxPrice=1000000&minBedrooms=1&maxBedrooms=3&displayPropertyType=houses&maxDaysSinceAdded=7&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false
bot3 = ScrapeWebsite(site_url = 'https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=REGION%5E93961&insId=1&radius=0.25&minPrice=50000&maxPrice=1000000&minBedrooms=1&maxBedrooms=3&displayPropertyType=houses&maxDaysSinceAdded=7&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false')
   
filter_xpath = bot3.find_node_xpath(tagname = 'div', 
                                attribute = 'class', 
                                value = 'filtersBar-moreText',
                                list_item ='',
                                display_label='')
bot3.accept_element(filter_xpath)

#On filter dropdown page set the filter options
#Filter Must Have options: Garden,Parking,New Home,Retirement Home,Buying Schemes,Auction Property
#Filter Dont Show options: New Home,Retirement Home,Buying Schemes
#works bot3.find_filter_elements_using_span(tagname ='div', attribute ='class', value  = 'multiSelect-label', labels = ['Garden','Parking'])
bot3.find_filter_elements_using_linktext(tagname ='div', 
                                        tag_attribute ='class', 
                                        tag_attribute_value  = 'multiSelect-option multiSelect-option--selected', 
                                        object_attribute='data-test',
                                        object_attribute_value  = 'mustHave')  
#bot3.accept_element_containing_text(self, element_type ='div', element_text = 'mustHave', req_dropdown_element_index ='Home')