# Web Scraping Project

This repository contains solutions to several web scraping challenges using various techniques. The goal is to extract information from a target website and answer specific questions regarding its content. Below is a description of the problems solved, the tools used, and how to run the scripts to extract the necessary data.

## Problems Solved

### 1. Number of Books and Average Price in Each Category
- **Problem**: For each category on the website, determine the total number of books and calculate the average price of the books listed.
- **Solution**: Web scraping is used to extract data about books, including their price and category, from the website. The script categorizes the books and calculates the required metrics for each category.

### 2. Number of Pages on the Website
- **Problem**: Determine how many pages are available on the website.
- **Solution**: After logging into the website, the scraper navigates through the pagination structure and counts the total number of pages available.

### 3. Number of Citations on a Specific URL
- **Problem**: Find the total number of citations listed on a given URL.
- **Solution**: A scraping script is designed to extract all citations from the URL and count how many are available.

### 4. First Citation on a Given URL
- **Problem**: Retrieve the first citation from a specific URL.
- **Solution**: The script identifies and extracts the first citation from the page and displays it.

### 5. Fifth Citation on a Given URL
- **Problem**: Retrieve the fifth citation from a specific URL.
- **Solution**: The script extracts the fifth citation and returns it as output.

### 6. Most Repetitive Tag on the Page
- **Problem**: Identify the most repetitive tag used on the page.
- **Solution**: The script scrapes the page, counts the occurrences of each tag, and identifies the most frequently used one.

### 7. Unique Albert Einstein Citation on Music
- **Problem**: Find the unique citation from Albert Einstein about music by submitting a search form.
- **Solution**: The script interacts with a form on the webpage, submits the relevant search query for Albert Einstein quotes about music, and extracts the unique result.

### 8. Estimated Time to Scrape the Entire Website
- **Problem**: Estimate how long it would take to scrape the entire content of the website.
- **Solution**: The script measures the time taken to scrape a sample of the content and extrapolates the result to estimate the time required to scrape the entire website.

## Tools and Technologies

- **Python**: The primary programming language used for this project.
- **Libraries**:
  - `BeautifulSoup`: For parsing HTML and extracting data from web pages.
  - `Requests`: For sending HTTP requests to the website and fetching page content.
  - `Selenium`: For handling dynamic web pages and form submissions that require interaction.
  - `Pandas`: For data analysis, including calculating averages and working with structured data.
  - `time`: To measure the time taken for scraping tasks.

## Prerequisites

Before running the scripts, ensure you have the following installed on your system:

- Python 3.x
- Required Python packages (can be installed using the command below):

```bash
pip install -r requirements.txt
