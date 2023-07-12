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
            title_element = element.select_one('.titleline > a')
            title = title_element.text.strip() if title_element else 'N/A'

            order_element = element.select_one('.rank')
            order = order_element.text.strip().replace(".", '') if order_element else 'N/A'

            comments_element = element.find_next('tr').select('.subtext a:nth-of-type(3)')

            # Parse the comment number and set to 0 if there are no comments
            if comments_element:
                comments = comments_element[-1].text.strip().replace("\xa0comments", '').replace("\xa0comment",'')
                if not comments.isdigit():
                    comments = 0
                else:
                    comments = int(comments)
            else:
                comments = 0

            points_element = element.find_next('tr').select_one('.score')
            points = points_element.text.strip().replace(" points", '').replace(" point", '') if points_element else 'N/A'

            # Appends selection to result
            entries.append({'title': title, 'order': order, 'comments': comments, 'points': points})

        return entries
    except Exception as e:
        print('Error:', str(e))
        return []


# Usage
entries = scrape_webpage()
print('\n******************************************* COMPLETE DATA ***************************************')
for entry in entries:
    print(entry)

# Filter all previous entries with more than five words in the title ordered by the number of comments first.
filtered_entries = [entry for entry in entries if len(entry['title'].split()) > 5]
filtered_entries.sort(key=lambda x: int(x['comments']), reverse=True)

print('\n******************************* WORDS > 5 ORDERED BY MOST COMMENTS *******************************')
for entry in filtered_entries:
    print(entry)

# Filter all previous entries with less than or equal to five words in the title ordered by points.
filtered_entries = [entry for entry in entries if len(entry['title'].split()) <= 5]
filtered_entries.sort(key=lambda x: int(x['points']) if x['points'].isdigit() else 0, reverse=True)

print('\n******************************* WORDS <= 5 ORDERED BY MOST POINTS ********************************')
for entry in filtered_entries:
    print(entry)