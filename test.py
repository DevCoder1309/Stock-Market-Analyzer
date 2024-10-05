from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()  

try:
    url = 'https://www.equitypandit.com/historical-data/RELIANCE'
    
    while True:
        driver.get(url)
        
        time.sleep(5)  
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        stock_open_price = soup.find('p', {'id': 'BSE_OPEN_PRICE'})
        stock_high_low_price = soup.find('p', {'id': 'BSE_TODAYS_HIGH_LOW'})

        stock_open_new_price = stock_open_price.text.strip()
        stock_open_new_high_low = stock_high_low_price.text.strip()

        if (stock_open_price and stock_high_low_price):
            
            
            if stock_open_new_price != old_price or stock_open_new_high_low != :
                # Any Changes chall be reflected here and price prediction should be placed here
                print(f"Current Price: {stock_open_new_price}")
                old_price = stock_open_new_price
            else:
                print(f"Price remains the same: {stock_open_new_price}")
        else:
            print("Stock price not found.")
        
        time.sleep(60) 
finally:
    driver.quit() 