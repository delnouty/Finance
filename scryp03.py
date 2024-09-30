import requests
from bs4 import BeautifulSoup
import csv

def scrape_page(url, csvwriter, write_header):
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

                    # Write the header only for the first page
                    if write_header:
                        header = [th.text for th in rows[0].find_all('th')]
                        csvwriter.writerow(header)

                    # Write the data rows
                    for row in rows[1:]:
                        data = [td.text for td in row.find_all('td')]
                        csvwriter.writerow(data)
                else:
                    print('No table found on', url)
            else:
                print('Error:', response.status_code)
    except requests.RequestException as e:
        print('Request failed:', e)

base_url = "https://finance.yahoo.com/markets/stocks/gainers/"
urls = [f"{base_url}?offset={i*25}&count=25" for i in range(10)]

with open('market_data10.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    for i, url in enumerate(urls):
        scrape_page(url, csvwriter, write_header=(i == 0))

print('Data extracted and saved to market_data01.csv')