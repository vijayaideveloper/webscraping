# importing nessecery packages
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

data = []

for i in range(1,51):
    url = f"http://books.toscrape.com/catalogue/page-{i}.html"
    half_url = "http://books.toscrape.com/catalogue/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find("ol", class_="row").find_all("li")
    for book in books:
        link = book.find("div", class_="image_container").find("a")['href']
        full_url = half_url+link
        
        data.append({
            "Link":full_url
        })
    print(f"Page : {i} is completed !")

len(data)

df = pd.DataFrame(data)
df.head()

completed_data = []

# Title, Price, Stocks,Tax, UPC
for i,link in df.iterrows():
    url2 = link['Link']
    response2 = requests.get(url2)
    soup = BeautifulSoup(response2.text, "html.parser")
    name = soup.find("div", class_="product_main").find("h1").text
    price = soup.find("div", class_="product_main").find("h1").find_next_sibling("p").text
    stocks = soup.find("div", class_="product_main").find("p").find_next_sibling("p").text.strip()
    stock = stocks.split('(')[1]
    stock = stock.replace(")", "")
    table = soup.find('table', class_='table') # Finds the table
    rows = table.find_all('tr')
    tax = rows[4].find('td').text
    upc = soup.find("table", class_="table").find("td").text

    completed_data.append({
        "Title":name,
        "Price":price,
        "Stocks":stock,
        "Tax":tax,
        "UPC":upc
    })
    print(f"Scraped Book {i+1} : {name} is Collected !")
    time.sleep(1)


final_data = pd.DataFrame(completed_data)

final_data.to_csv("Book_Details.csv")