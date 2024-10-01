from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from collections import Counter
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure the option to run the browser in headless mode (no window displayed)
chrome_options = Options()
chrome_options.add_argument("--headless")

# Path to your WebDriver
service = Service(executable_path="..\\drivers\\chromedriver.exe")

# Initialize the driver with the options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the page with Selenium
driver.get("https://quotes.toscrape.com/tableful/")

# Wait until the tags are present on the page
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td/a")))

# Retrieve all <td> cells that contain tags
tags_elements = driver.find_elements(By.XPATH, "//td[contains(text(), 'Tags:')]/a")

# Extract the text from the links (the names of the tags)
tags = [tag.text for tag in tags_elements]

# Count the occurrences of each tag
tag_counts = Counter(tags)

# Find the most repetitive tag
most_common_tag = tag_counts.most_common(1)[0]  # Returns the most frequent tag

print("Most repetitive tag:", most_common_tag[0])
print("Number of occurrences:", most_common_tag[1])

# Close the driver
driver.quit()

