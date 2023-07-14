# Web Crawler

This is a simple web crawler application that scrapes a webpage and performs filtering on the scraped data
based on the number of words in the title. The filtered results are then saved to JSON files.

Web Crawler consists of two main files:

- `main.py`: This is the main script that utilizes the `WebCrawler` class to perform web scraping and filtering operations.
  It retrieves data from a specified webpage, applies filters based on the number of words in the title, and saves the filtered results to JSON files.

- `WebCrawler.py`: This file contains the `WebCrawler` class, which encapsulates the web scraping functionality.
  It uses the Beautiful Soup library to parse the HTML content of a webpage and extract relevant information such as the title, order, number of comments, and points for each entry.

## Prerequisites

- Python 3.x
- Beautiful Soup library (bs4)
- Requests library

### Acknowledgments
  [Beautiful Soup]([url](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)) - Python library for web scraping
  [Requests]([url](https://requests.readthedocs.io/en/latest/)) - Python library for making HTTP requests


#### Contact
  For any questions or inquiries, please contact albertogr.contacto@gmail.com
