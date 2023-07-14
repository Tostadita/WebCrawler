import requests
import json
from typing import Dict, Any, Union, List
from bs4 import BeautifulSoup


class WebCrawler:
    def __init__(self, url: str):
        self.url = url

    def scrape_webpage(self):
        try:
            # Establish connection and fetch html data
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')

            entries = []
            entry_elements = soup.select('.athing')[:30]  # Extract first 30 entries
            for element in entry_elements:
                title_element = element.select_one('.titleline > a')
                title = title_element.text.strip() if title_element else 'N/A'

                order_element = element.select_one('.rank')
                order = order_element.text.strip().replace(".", '') if order_element else 'N/A'

                comments_element = element.find_next('tr').select('.subtext a:nth-of-type(3)')

                # Parse the comment number and set to 0 if there are no comments
                if comments_element:
                    # Remove filler data from comments
                    comments = comments_element[-1].text.strip().replace("\xa0comments", '').replace("\xa0comment", '')
                    if not comments.isdigit():
                        comments = 0
                    else:
                        comments = int(comments)
                else:
                    comments = 0

                points_element = element.find_next('tr').select_one('.score')

                points = points_element.text.strip().replace(" points", ''). \
                    replace(" point", '') if points_element else 'N/A'

                # Appends selection to result
                entries.append({'title': title, 'order': order, 'comments': comments, 'points': points})

            return entries
        except Exception as e:
            print('Error:', str(e))
            return []

    def save_to_file(self, filename: str, data: Union[Dict[str, Any], List[str]]):
        # TODO:Check if file already exists  #
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


# if __name__ == '__main__':
#     url = 'https://news.ycombinator.com/'
#     session = WebCrawler(url)
#     session.main()


