from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_quote_count(url):
    # Set up the web driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Open the URL
        driver.get(url)
        
        # Find all quote elements
        quotes = driver.find_elements(By.CLASS_NAME, 'quote')
        
        return len(quotes)
    finally:
        # Close the web driver
        driver.quit()

url = 'https://quotes.toscrape.com/scroll'
quote_count = get_quote_count(url)
print(f'Total number of quotes: {quote_count}')
