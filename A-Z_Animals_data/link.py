from bs4 import BeautifulSoup
import pandas as pd
import requests
import time



letters = 'abcdefghijklmnopqrstuvwxyz'
for i in letters:
    url = f'https://a-z-animals.com/animals/animals-that-start-with-{i}/'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }

    response = requests.get(url, headers=headers)
    time.sleep(1)

    soup = BeautifulSoup(response.text,'html.parser')

    links = soup.find('div', class_='link-list link-list--cols-3').find_all('a')

    data = []

    for link in links:
        print(link['href'])

        data.append({
            "Links":link['href'].strip()
        })

    df = pd.DataFrame(data)
    df.to_csv(f'datalinks/{i}-animal-{len(links)}.csv',index=False)
    print()
    print(f'{i}-Link Saved !')
    print()
    data.clear()
