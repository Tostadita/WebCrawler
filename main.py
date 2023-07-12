import requests
from bs4 import BeautifulSoup


def scrape_webpage():
    try:
        # Stablish connection and fetch html data
        response = requests.get('https://news.ycombinator.com/')
        soup = BeautifulSoup(response.text, 'html.parser')

        entries = []
        entry_elements = soup.select('.athing')[:30]  # Extract first 30 entries
        for element in entry_elements:
            title_element = element.select_one('.titleline')
            title = title_element.text.strip() if title_element else 'N/A'

            order_element = element.select_one('.rank')
            order = order_element.text.strip() if order_element else 'N/A'

            comments_element = element.find_next('tr').select('.subtext a:nth-of-type(3)')
            comments = comments_element[-1].text.strip().replace("\xa0", ' ') if comments_element else 'N/A'

            points_element = element.find_next('tr').select_one('.score')
            points = points_element.text.strip() if points_element else 'N/A'

            # Appends selection to result
            entries.append({'title': title, 'order': order, 'comments': comments, 'points': points})

        return entries
    except Exception as e:
        print('Error:', str(e))
        return []


# Usage
entries = scrape_webpage()
for entry in entries:
    print(entry)

# TODO: Filter data