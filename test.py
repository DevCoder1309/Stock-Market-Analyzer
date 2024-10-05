from selenium import webdriver
from bs4 import BeautifulSoup
import time
from stock_analysis_pred.i

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

        arr = list(stock_open_new_high_low.split(' / '))
        print(arr)
        stock_high_price = float(arr[1])
        stock_low_price = float(arr[0])
        if (stock_open_price and stock_high_low_price):
            print(f"Current Price: {stock_open_new_price}, {stock_high_price}, {stock_low_price}")
        else:
            print("Stock price not found.")
        
        time.sleep(60) 
finally:
    driver.quit() 