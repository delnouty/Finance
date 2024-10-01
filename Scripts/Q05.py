from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the web driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL of the page to scrape
url = "https://quotes.toscrape.com/js/page/10/"

# Open the page
driver.get(url)

# Find the first quote element
first_quote = driver.find_element(By.CLASS_NAME, 'quote')

# Extract the text of the quote and the author
quote_text = first_quote.find_element(By.CLASS_NAME, 'text').text
quote_author = first_quote.find_element(By.CLASS_NAME, 'author').text

# Print the quote and the author
print(f"Quote: {quote_text}")
print(f"Author: {quote_author}")

# Close the web driver
driver.quit()
