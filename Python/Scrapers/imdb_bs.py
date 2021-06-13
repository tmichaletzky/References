import requests
from bs4 import BeautifulSoup
import csv

websites = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250',
           'https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250',
           'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm',
           'https://www.imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv']
            #websites to scrape
for website in websites:
    #lists we will store data
    titles = list()
    years = list()
    ratings = list()
    seens = list()

    source = requests.get(website).text #fetch data

    soup = BeautifulSoup(source, 'lxml') #extracted text

    #now we should find data stored in soup
    tbody = soup.tbody #top 250 is under tag 'tbody'
    entries = tbody.find_all('tr') #where entries -movies- are separated with tag 'tr'

    for td in entries:
        title_tmp = td.find_all('td', class_ = 'titleColumn') #fetch appropiate lines
        rating_tmp = td.find_all('td', class_ = 'ratingColumn imdbRating')
        seen_tmp = td.find_all('td', class_ = 'ratingColumn')

        for _ in title_tmp:
            title = _.a.text #extract title
            titles.append(title) #append to final list

            year = _.span.text
            years.append(year)

        for _ in rating_tmp:
            if _.text is None:
                rate = ''
            else:
                rate = _.text.strip()
            ratings.append(rate)


    file_title = soup.title.text + '.csv'

    file = open(file_title, 'w', encoding='utf-8')
    writer = csv.writer(file)

    writer.writerow(['Title', 'Year', 'Rate'])

    for item in zip(titles, years, ratings):
        writer.writerow(item)
        print(item)

    file.close()
