from WebCrawler import WebCrawler


def main(url: str):
    # Instantiate webcrawler class
    webcrawler = WebCrawler(url)
    entries = webcrawler.scrape_webpage()

    print('\n******************************************* COMPLETE DATA ***************************************')

    webcrawler.save_to_file('complete_data.json', entries)
    for entry in entries:
        print(entry)

    # Filter all previous entries with more than five words in the title ordered by the number of comments first.
    filtered_entries = [entry for entry in entries if len(entry['title'].split()) > 5]
    filtered_entries.sort(key=lambda x: int(x['comments']), reverse=True)

    print('\n******************************* WORDS > 5 ORDERED BY MOST COMMENTS *******************************')

    webcrawler.save_to_file('filtered_by_comments.json', filtered_entries)
    for entry in filtered_entries:
        print(entry)

    # Filter all previous entries with less than or equal to five words in the title ordered by points.
    filtered_entries = [entry for entry in entries if len(entry['title'].split()) <= 5]
    filtered_entries.sort(key=lambda x: int(x['points']) if x['points'].isdigit() else 0, reverse=True)

    print('\n******************************* WORDS <= 5 ORDERED BY MOST POINTS ********************************')

    webcrawler.save_to_file('filtered_by_points.json', filtered_entries)
    for entry in filtered_entries:
        print(entry)


if __name__ == '__main__':
    main('https://news.ycombinator.com/')