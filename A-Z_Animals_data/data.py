from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import glob
import os

folder_path='datalinks'
csv_files = glob.glob(os.path.join(folder_path,"*.csv"))


l=19
for csv_file in csv_files:
    data = pd.read_csv(csv_file)

    animal_data=[]
    print(f'{l} is Collecting 🍌')
    m=1
    for link in data['Links']:

        url = f'{link}'
        headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Accept-Language": "en-US,en;q=0.9",
            }

        response = requests.get(url, headers=headers)
        #time.sleep(1)

        Soup = BeautifulSoup(response.text, 'html.parser')
        
        
        container = Soup.find('div',id='container')
        try:
            name = container.find('h1', class_='site-hero__title').text.strip()
        except:
            name = ''
        print(f'{m}. {name}')
        try:
            scifi_name = container.find('p', class_='site-hero__scientific').text.strip()
        except:
            scifi_name = ''

        glance = container.find('div', class_='enc-quick-stats__grid')
        try:
            diet = glance.select_one('div:nth-of-type(1)').find('a').text.strip()
        except:
            diet=''
        try:
            activity = glance.find('div', class_='enc-quick-stats__item--activity').find('a').text.strip()

        except:
            activity=''
        
        try:
            lifespan = glance.select_one('div:nth-of-type(3)').find('span', class_='enc-quick-stats__value').text.strip()
        except:
            lifespan=''

        try:
            weight = glance.select_one('div:nth-of-type(4)').find('span', class_='enc-quick-stats__value').text.strip()
        except:
            weight=''
        
        try:
            status = glance.select_one('div:nth-of-type(5)').find('a').text.strip()
        except:
            status=''

        try:
            scifi_class = container.find('dl', class_='enc-classification__taxonomy')
        except:
            scifi_class=''
        try:
            kingdom = scifi_class.select_one('div:nth-of-type(1)').find('dd').text.strip()
        except:
            kingdom=''
        try:
            phylum = scifi_class.select_one('div:nth-of-type(2)').find('dd').text.strip()
        except:
            phylum=''
        try:
            ani_class = scifi_class.select_one('div:nth-of-type(3)').find('dd').text.strip()
        except:
            ani_class=''
        try:
            order = scifi_class.select_one('div:nth-of-type(4)').find('dd').text.strip()
        except:
            order=''
        try:
            family = scifi_class.select_one('div:nth-of-type(5)').find('dd').text.strip()
        except:
            family=''
        try:
            genus = scifi_class.select_one('div:nth-of-type(6)').find('dd').text.strip()
        except:
            genus=''
        try:
            species = scifi_class.select_one('div:nth-of-type(7)').find('dd').text.strip()
        except:
            species=''

        try:
            founded_countries = container.find('h3', class_='enc-map__country-list-title').text.strip()
        except:
            founded_countries=''

        animal_data.append({
            "name":name,
            "scifi_name":scifi_name,
            "diet":diet,
            "activity":activity,
            "lifespan":lifespan,
            "weight":weight,
            "status":status,
            "kingdom":kingdom,
            "phylum":phylum,
            "class":ani_class,
            "order":order,
            "family":family,
            "genus":genus,
            "species":species,
            "founded_countries_count":founded_countries
        })
        
        m+=1
        
    df = pd.DataFrame(animal_data)

    df.to_csv(f'animal_data/{l}st-list-animals.csv',index=False)
    animal_data.clear()
    print(f'Collected Successfully 🥁')
    print()
    l+=1

