from  utils.ScrapeWebsite import ScrapeWebsite
~Date : 11 November 2022

if __name__ == '__main__':
    #On RightMove website
 '''   bot = ScrapeWebsite(site_url = 'https://www.rightmove.co.uk/')

    ################On Website page 1:################
    # 1a. find cookie button and click accept cookies
    cookies_xpath= bot.find_element_xpath(tagname = 'button', 
                                        tag_attribute = 'class', 
                                        tag_value = 'optanon-allow-all accept-cookies-
                                        button',
                                        list_item ='',
                                        display_label='')
    print(cookies_xpath)                        
    bot.accept_element(cookies_xpath)
    
   
    # 1b. enter the search location either - site acepts a location name or a postcode
    # 1b. get the search bar xpath
    location_searchbar_xpath = bot.find_element_xpath(tagname = 'input', 
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
    
    location_suggested_list_xpath=bot.find_element_xpath(tagname = 'ul', 
                                                tag_attribute = 'class', 
                                                tag_value = 'ksc_resultsList',
                                                list_item = 'li[1]',
                                                display_label='') #accepts the first item in the suggested list
    print(f"location suggested list xpath= {location_suggested_list_xpath}")
    bot.accept_element(location_suggested_list_xpath)

    #time.sleep(5000)

    # 1f. Find FOR SALE button and click to display for sale properties
    forsale_xpath=bot.find_element_xpath (tagname = 'button', 
                                        tag_attribute = 'class', 
                                        tag_value = 'ksc_button large primary searchPanelControls',
                                        list_item = '',
                                        display_label='')                 
    print(forsale_xpath)     
    bot.accept_element_containing_text(element_type='button', element_text = 'For Sale', req_dropdown_element_index = 0) 
                           
############# On website page 2 ################
# https://www.rightmove.co.uk/property-for-sale/search.html?searchLocation=NW%20(Postcode%20Area)&useLocationIdentifier=true&locationIdentifier=REGION%5E93961&buy=For+sale
    
    #2a. Set the search radius for the location specified  
    #bot.set_dropdown_using_select_ByID(element_attribute='By.ID', element_value='radius', dropdown_selection='0.25')
    bot.set_dropdown_using_select_option(element_attribute='name', 
                                        element_name ='radius', 
                                        dropdown_string = 'Within 1/2 mile')
    #works bot.set_dropdown_from_LoV(element_value = 'radius',dropdown_value = '0.25')
    

    #2b. Set the min price for the properties searched   
    bot.set_dropdown_from_LoV_byID(element_value = 'minPrice',dropdown_value = '50000') 

    #2c. Set the max price for the properties searched   
    bot.set_dropdown_from_LoV_byID(element_value = 'maxPrice',dropdown_value = '1000000')  
    
    #2d. Set the min bedrooms for the properties searched   
    bot.set_dropdown_from_LoV_byID(element_value = 'minBedrooms',dropdown_value = '1')  

    #2e. Set the max bedrooms for the properties searched   
    bot.set_dropdown_from_LoV_byID(element_value = 'maxBedrooms',dropdown_value = '3')  

    #2f. Set the max bedrooms for the properties searched   
    bot.set_dropdown_from_LoV_byID(element_value = 'displayPropertyType',dropdown_value = 'houses')

    #2g. Set the max bedrooms for the properties searched   
    bot.set_dropdown_from_LoV_byID(element_value = 'maxDaysSinceAdded',dropdown_value = '7') 
    
    #2h. Set the include sold and STC to ON or OFF. ON includes sold and STC in listings
    bot.accept_element_using_contains(tagname='span',
                                        tag_attribute='class',
                                        tag_value  = 'tickbox--indicator',
                                        required_value = 'Off')#set this to on or off
    
    
    #2h. Select the find property button
    findproperty_xpath= bot.find_element_xpath(tagname = 'button', 
                                        tag_attribute = 'class', 
                                        tag_value = 'button touchsearch-button touchsearch-primarybutton',
                                        list_item ='',
                                        display_label='')
                      
    bot.accept_element(findproperty_xpath)
    
################ On website property listings page - Website page 3 ################

# rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=REGION%5E93961&insId=1&radius=0.25&minPrice=50000&maxPrice=1000000&minBedrooms=1&maxBedrooms=3&displayPropertyType=houses&maxDaysSinceAdded=7&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false
    #bot3 = ScrapeWebsite(site_url = 'https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=REGION%5E93961&insId=1&radius=0.25&minPrice=50000&maxPrice=1000000&minBedrooms=1&maxBedrooms=3&displayPropertyType=houses&maxDaysSinceAdded=7&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false')
    #3a. select the filter option on the right of the black secondary menu bar along the top of page  
    filter_xpath = bot.find_element_xpath(tagname = 'div', 
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
    done_xpath = bot.find_element_xpath(tagname = 'button', 
                                    tag_attribute = 'data-test', 
                                    tag_value = 'apply-filters-button',
                                    list_item ='',
                                    display_label='')
    print(done_xpath)
    bot.accept_element(done_xpath)
    bot.sleep(2) '''

################ On website property listings returned page after filters are applied - Website page 4 ################
  
    
#https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E93961&maxBedrooms=3&minBedrooms=1&maxPrice=1000000&minPrice=50000&radius=0.25&propertyTypes=detached%2Csemi-detached%2Cterraced&maxDaysSinceAdded=7&includeSSTC=false&mustHave=garden%2Cparking&dontShow=retirement%2CsharedOwnership&furnishTypes=&keywords=
bot4 = ScrapeWebsite(site_url = 'https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E93961&maxBedrooms=3&minBedrooms=1&maxPrice=1000000&minPrice=50000&radius=0.25&propertyTypes=detached%2Csemi-detached%2Cterraced&maxDaysSinceAdded=7&includeSSTC=false&mustHave=garden%2Cparking&dontShow=retirement%2CsharedOwnership&furnishTypes=&keywords=')

#4a. define the listing order required - (2)Highest Price,(1)Lowest Price, (6)Newest Listed, (10)Oldest Listed
#works bot4.set_dropdown_from_LoV_byID(element_value ='sortType', dropdown_value = '6')
#works bot4.set_dropdown_using_select_ByID( element_attribute = 'ID', element_value ='sortType', dropdown_selection ='1')
bot4.set_dropdown_using_select_option(element_attribute='ID', 
                                    element_name ='sortType', 
                                    dropdown_string = 'Lowest Price')

#4b. extract the list of propert returned by the search
#//div[@class="l-searchResults/div"]./div
properties_found=[]
properties_found_url = bot4.find_items_in_search_listing(search_container_xpath = '//*[@id="l-searchResults"]/div/div', 
                                    search_container_child_tag='./div',
                                    page_control_tagname = 'div', 
                                    page_control_element_attribute ='class', 
                                    page_control_element_name ='pagination-controls', 
                                    page_control_label ='Next')
print(*properties_found_url)
print(f" No of property urls found: {len(properties_found_url)}")
                                 
bot4.extract_property_details(search_urls = properties_found_url)

################ On property detail page - testing only ################
'''#https://www.rightmove.co.uk/properties/128812670#/?channel=RES_BUY
bot5 = ScrapeWebsite(site_url = 'https://www.rightmove.co.uk/properties/128812670#/?channel=RES_BUY')

property_info=bot5.find_element_xpath_using_contains(tagname = 'meta',
                                                        tag_attribute= 'itemprop', 
                                                        tag_value ='content',
                                                        required_value ='')
print(property_type)
# doe snot work print(property_type.value)
print(property_type.get_attribute('text'))
print(property_type.get_attribute('value'))


property_address=bot5.find_element_xpath_using_contains(tagname = 'h1',
                                                        tag_attribute= 'itemprop', 
                                                        tag_value ='streetAddress',
                                                        required_value ='')
print(property_address.text)

property_info=[]
property_info =bot5.find_list_of_elements_xpath_using_contains(tagname = 'div',
                                                        tag_attribute= 'class', 
                                                        tag_value ='_4hBezflLdgDMdFtURKTWh',
                                                        required_value ='')

select_element_from_list_of_elements (self, list_of_elements = property_info, select_criteria='')
print(property_type.text)


property_rooms=bot5.find_element_xpath_using_contains(tagname = 'p',
                                                        tag_attribute= 'class', 
                                                        tag_value ='_1hV1kqpVceE9m-QrX_hWDN ',
                                                        required_value ='')
print(property_rooms.text) 

bot5.sleep(500)'''
