import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/"
categories_url = "https://books.toscrape.com/index.html"

# Initialize a session
session = requests.Session()
response = session.get(categories_url)
soup = BeautifulSoup(response.text, 'html.parser')

categories = soup.find('ul', class_='nav nav-list').find('ul').find_all('li')

books_data = []

for category in categories:
    category_name = category.find('a').text.strip()
    category_link = base_url + category.find('a')['href']
    page = 1
    
    while True:
        # Construct the URL for each page
        if page == 1:
            page_url = category_link
        else:
            page_url = category_link.replace('index.html', f'page-{page}.html')
            print(page_url)
        
        response = session.get(page_url)
        if response.status_code != 200:
            pass
            #print(f"Failed to retrieve page {page} for category {category_name}")
            break
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        books = soup.find_all('article', class_='product_pod')
        if not books:
            break
        
        for book in books:
            title = book.find('h3').find('a')['title']
            price = book.find('p', class_='price_color').text
            price = (price[1:])  # Remove the currency symbol and convert to float
            
            books_data.append({
                'title': title,
                'category': category_name,
                'price': price
            })
        
        page += 1

# Create a DataFrame
df = pd.DataFrame(books_data)

# Display the DataFrame
print(df)

# Save the DataFrame to a CSV file
df.to_csv('books_data.csv', index=False)

# Check if DataFrame is empty
if df.empty:
    print("The DataFrame is empty. Please check the scraping logic.")
else:
    print("DataFrame created successfully.")

# Check if DataFrame is empty
if df.empty:
    print("The DataFrame is empty. Please check the scraping logic.")
else:
    print("DataFrame created successfully and saved to 'books_data.csv'.")

# Extract symbols starting from the second character
df['price'] = df['price'].apply(lambda x: x[1:])

# Convert the extracted symbols to numeric values
df['price'] = pd.to_numeric(df['price'])

# Display the updated DataFrame
print(df.head())

# Group by 'category' and calculate the average price
avg_price_per_category = df.groupby('category')['price'].mean().reset_index()

# Rename the columns for clarity
avg_price_per_category.columns = ['category', 'average_price']

# Display the result
print(avg_price_per_category)

# Group by 'category' and calculate the average price and count of books
category_stats = df.groupby('category').agg(
    average_price=('price', 'mean'),
    book_count=('price', 'size')
).reset_index()

# Display the result
print(category_stats)