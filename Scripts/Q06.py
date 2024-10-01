from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Navigate to the page
    driver.get("https://quotes.toscrape.com/js-delayed/page/5/")

    # Wait for the quotes to load
    driver.implicitly_wait(10)  # Wait up to 10 seconds

    # Find all quotes on the page
    quotes = driver.find_elements(By.CLASS_NAME, "quote")

    # Check if there are at least 5 quotes
    if len(quotes) >= 5:
        # Get the fifth quote
        fifth_quote = quotes[4].text
        print("Fifth quote:", fifth_quote)
    else:
        print("There are not enough quotes on this page.")

finally:
    # Close the browser
    driver.quit()
