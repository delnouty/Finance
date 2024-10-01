from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Set up the Selenium WebDriver (make sure to have the appropriate driver installed)
driver = webdriver.Chrome()  # You can use other drivers like Firefox, Edge, etc.

# Open the webpage
url = 'https://quotes.toscrape.com/tableful/'
driver.get(url)

# Get the page source after JavaScript has rendered the content
page_source = driver.page_source

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Find the table with the class 'table'
table = soup.find('table', {'class': 'table'})

if table:
    # Extract the first row of the table
    first_row = table.find('tr')
    
    if first_row:
        # Extract the text from each cell in the first row
        first_row_text = [cell.get_text(strip=True) for cell in first_row.find_all('td')]
        
        print("Contents of the first line in the 'Top ten tags' table:")
        for text in first_row_text:
            print(text)
    else:
        print("First row not found in the table.")
else:
    print("Table with class 'table' not found.")

# Close the browser
driver.quit()
