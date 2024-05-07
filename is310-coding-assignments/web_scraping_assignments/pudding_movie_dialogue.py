import pandas as pd
import requests
import csv
from bs4 import BeautifulSoup

df = pd.read_csv('cleaned_pudding_data.csv')

links = df['link']

with open('pudding_movie_dialogue.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Link', 'Script'])
    for link in links:
        response = requests.get(link)
        if response.status_code != 200:
            continue
        dialogue = BeautifulSoup(response.text, "html.parser")
        dialogue.prettify()
        script = dialogue.get_text()[:1000]
        writer.writerow([link, script])