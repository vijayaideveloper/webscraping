from bs4 import BeautifulSoup
import requests
import pandas as pd
import time


url = "https://www.bollymoviereviewz.com/2022/02/tamil-box-office-collection-kollywood-report-verdict.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url, headers=headers)

time.sleep(2)

Soup = BeautifulSoup(response.text, "html.parser")
movies = Soup.find('table', class_='bordered').find_all('tr')[1:]

data = []


if movies:
    i = 1
    for movie in movies:
        print(f'Movie {i}')
        try:
            movie_name = movie.find('td').find('strong').text.strip()
            #col2 = row.select_one('td:nth-of-type(2)')
            box_office = movie.select_one('td:nth-of-type(2)').text.strip()
            budget = movie.select_one('td:nth-of-type(3)').text.strip()
            verdict = movie.select_one('td:nth-of-type(4)').text.strip()
        except:
            movie_name = movie.find('td').find('b').text.strip()
            #col2 = row.select_one('td:nth-of-type(2)')
            box_office = movie.select_one('td:nth-of-type(2)').text.strip()
            budget = movie.select_one('td:nth-of-type(3)').text.strip()
            verdict = movie.select_one('td:nth-of-type(4)').text.strip()


        '''print("Movie Name",movie_name,
            "Box Office",box_office,
            "Budget",budget,
            "Verdict",verdict)'''
        
        data.append({
            "Movie Name":movie_name,
            "Box Office":box_office,
            "Budget":budget,
            "Verdict":verdict
        })

        print()
        time.sleep(1)
        i += 1


else:
    print('Not Found')

df = pd.DataFrame(data)

df.to_csv("Moive_box_office_data.csv", index=False)
print()
print("Data is Saved !")