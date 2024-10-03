from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()  

old_price = None

try:
    url = 'https://www.equitypandit.com/historical-data/RELIANCE'
    
    while True:
        driver.get(url)
        
        time.sleep(5)  
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        stock_price = soup.find('p', {'id': 'BSE_OPEN_PRICE'})

        if stock_price:
            current_price = stock_price.text.strip()
            if current_price != old_price:
                # Any Changes chall be reflected here and 
                print(f"Current Price: {current_price}")
                old_price = current_price
            else:
                print(f"Price remains the same: {current_price}")
        else:
            print("Stock price not found.")
        
        time.sleep(60) 
finally:
    driver.quit() 