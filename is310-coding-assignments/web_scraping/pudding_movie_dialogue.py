import bs4
import requests
import csv
import pandas as pd

df = pd.read_csv('cleaned_pudding_data.csv')

links = df['link']

with open('pudding_dialogues.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Link', 'Dialogue Text'])

    for link in links:
        response = requests.get(link)
        if response.status_code != 200:
            continue

    dialogue_soup = BeautifulSoup(response.text, 'html.parser')
    dialogue_soup.prettify()
    script = dialogue_soup.get_text()[:1000]

    writer.writerow([link,script])
