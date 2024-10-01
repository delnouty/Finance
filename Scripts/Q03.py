import random
import string
import requests
from bs4 import BeautifulSoup

def generate_random_string(length, characters):
    return ''.join(random.choice(characters) for _ in range(length))

def generate_username(length=8):
    return generate_random_string(length, string.ascii_letters + string.digits)

def generate_password(length=12):
    return generate_random_string(length, string.ascii_letters + string.digits + string.punctuation)

def get_total_pages(session, base_url):
    page_number = 1
    while True:
        url = f"{base_url}/page/{page_number}/"
        response = session.get(url)
        if response.status_code != 200:
            break
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        if not quotes:
            break
        page_number += 1
    return page_number - 1

def scrape_quotes(session, base_url, total_pages):
    all_quotes = []
    for page in range(1, total_pages + 1):
        url = f"{base_url}/page/{page}/"
        response = session.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            all_quotes.append({'text': text, 'author': author})
    return all_quotes

# Generate a random username and password
random_username = generate_username()
random_password = generate_password()

print("Generated username:", random_username)
print("Generated password:", random_password)

# Your login credentials with the generated username and password
payload = {
    "username": random_username,
    "password": random_password
}

# URL of the login page
login_url = "https://quotes.toscrape.com/login"
main_page_url = "https://quotes.toscrape.com/"

# Create a session to persist the login
with requests.Session() as session:
    # Send a POST request to the login page with your credentials
    response = session.post(login_url, data=payload)

    # Print the status code of the POST request
    print("POST request status code:", response.status_code)

    # Check if login was successful
    if "Logout" in response.text:
        print("Login successful!")
        # Redirect to the main page
        main_page_response = session.get(main_page_url)
        print("Redirected to main page. Status code:", main_page_response.status_code)
        
        # Get the total number of pages
        total_pages = get_total_pages(session, main_page_url)
        print(f"Total number of pages: {total_pages}")

        # Scrape all quotes
        quotes = scrape_quotes(session, main_page_url, total_pages)
        print(f"Total number of quotes: {len(quotes)}")

        # Print the quotes
        #for quote in quotes:
        #    print(f"{quote['text']} - {quote['author']}")
    else:
        print("Login failed!")
