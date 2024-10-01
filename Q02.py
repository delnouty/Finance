import random
import string
import requests

def generate_random_string(length, characters):
    return ''.join(random.choice(characters) for _ in range(length))

def generate_username(length=8):
    return generate_random_string(length, string.ascii_letters + string.digits)

def generate_password(length=12):
    return generate_random_string(length, string.ascii_letters + string.digits + string.punctuation)

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

# Create a session to persist the login
with requests.Session() as session:
    # Send a POST request to the login page with your credentials
    response = session.post(login_url, data=payload)

    # Print the status code of the POST request
    print("POST request status code:", response.status_code)

    # Check if login was successful
    if "Logout" in response.text:
        print("Login successful!")
    else:
        print("Login failed!")
