import requests
from bs4 import BeautifulSoup
import pandas as pd
import yfinance as yf

def scrape_page(url):
    try:
        with requests.Session() as session:
            response = session.get(url)
            response.encoding = response.apparent_encoding

            if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, 'lxml')

                # Find the table
                table = soup.find('table')
                if table:
                    rows = table.find_all('tr')

                    # Extract header
                    header = [th.text for th in rows[0].find_all('th')]
                    data = []

                    # Extract data rows
                    for row in rows[1:]:
                        data.append([td.text for td in row.find_all('td')])

                    return pd.DataFrame(data, columns=header)
                else:
                    print('No table found on', url)
                    return pd.DataFrame()
            else:
                print('Error:', response.status_code)
                return pd.DataFrame()
    except requests.RequestException as e:
        print('Request failed:', e)
        return pd.DataFrame()

base_url = "https://finance.yahoo.com/markets/stocks/gainers/"
urls = [f"{base_url}?offset={i*25}&count=25" for i in range(10)]

all_data = pd.DataFrame()

for url in urls:
    page_data = scrape_page(url)
    all_data = pd.concat([all_data, page_data], ignore_index=True)

all_data.to_csv('market_data.csv', index=False)
print('Data extracted and saved to market_data.csv')

# Example of using yfinance to get stock data
stock_data = yf.download('AAPL', start='2023-01-01', end='2023-12-31')
stock_data.to_csv('apple_stock_data.csv')
print('Apple stock data saved to apple_stock_data.csv')
