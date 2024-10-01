from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Open the webpage
    driver.get("https://quotes.toscrape.com/search.aspx")

    # Select "Albert Einstein" from the Author dropdown
    author_select = Select(driver.find_element(By.ID, "author"))
    author_select.select_by_visible_text("Albert Einstein")

    # Select "music" from the Tag dropdown
    tag_select = Select(driver.find_element(By.ID, "tag"))
    tag_select.select_by_visible_text("music")

    # Submit the form
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    # Print the results
    quotes = driver.find_elements(By.CLASS_NAME, "quote")
    for quote in quotes:
        print(quote.text)

finally:
    # Close the WebDriver
    driver.quit()
