import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# this line of code hold the driver manager in cache without
#  having to download to Python path
driver = webdriver.Chrome(ChromeDriverManager().install())
from time import sleep

class Scraper:

    def __init__(self):
        
        self.interested_websites=["Zoopla"]
        self.interested_locations= ["London"]
        self.num_websites = len(self.interested_websites)   
        self.num_locations = len(self.interested_locations)
        self.myURL=""
        self.mydriver=""

    #function definition
    def get_website_data(self):
        ws_index=0
        loc_index =0
        while ws_index < self.num_websites:
            self.myURL = "https://www.zoopla.co.uk/new-homes/property/london/?q=London&results_sort=newest_listings&search_source=new-homes&page_size=25&pn=1&view_type=list"
            self.my_driver = driver.get(self.myURL)
            print(f"Driver =  {self.my_driver}")
             title = self.my_driver.title
             driver.implicitly_wait(0.5)
            #time.sleep(2)
            
            while loc_index < self.num_locations:
                mypath = driver.find_element(by=By.XPATH, value='//button')
                print(f"myelement = {myelement}")

if __name__ == '__main__':

    my_scrape = Scraper()
    my_scrape.get_website_data()


   