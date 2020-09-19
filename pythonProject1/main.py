from bs4 import BeautifulSoup #pip install bs4
from requests import get #pip install requests
import pandas as pd
import csv

URL = 'https://www.imdb.com/list/ls055386972'
page = get(URL)
bs = BeautifulSoup(page.content, 'html.parser')
csv_file=open('The 50 Best Movies Ever Made','w') #The csv file is written
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Titles','Runtime','Genre','Director'])
Tytul_filmu = []
Czas_trwania = []
Gatunki = []
Rezyser = []
for movies in bs.find_all('div', class_='lister-item-content'):
    Tytul_filmu.append(movies.find('h3', {'class': 'lister-item-header'}).a.text.strip())  #Nazwa filmu
    Czas_trwania.append(movies.find('span',{'class':'runtime'}).text.strip().split(' ')[0]) # czas trwania filmu
    Gatunki.append(movies.find('span', {'class': 'genre'}).text.strip())  # Gatunki
    #gatunek = movies.find('span', {'class': 'genre'}).text.strip().split(',')[0]  # Gatunek
    akapit = movies.find_all('p')
    director = akapit[2]
    Rezyser.append(director.a.text.strip())

data  = list(zip(Tytul_filmu,Czas_trwania,Gatunki,Rezyser))
df = pd.DataFrame(data,columns=['Titles','Runtime','Genre','Director'])
df.to_csv('The 50 Best Movies Ever Made.csv')
print('save to file')

csv_file.close()