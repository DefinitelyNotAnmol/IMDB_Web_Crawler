from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# Connecting to the Page, Grabbing Page
url = 'https://www.imdb.com/list/ls057433882/'
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

# HTML parsing
page_soup = soup(page_html, "html.parser")

# creating file
filename = str(page_soup.h1.text) + ".csv"
f = open(filename, "w")

headers = "Title,Year,Age Rating,Lenght,Genre,Rating,MetaScore\n"

f.write(headers)

# Grabbing all the movies
containers = page_soup.findAll("div", {"class": "lister-item-content"})

for container in containers:
    title = container.h3.a.text

    year = container.h3.findAll("span", {"class": "lister-item-year text-muted unbold"})
    year = year[0].text

    try:
        age_rating = container.p.span.text
    except:
        age_rating = 'N/A'

    lenght = container.p.findAll("span", {"class": "runtime"})
    lenght = lenght[0].text

    genre = container.p.findAll("span", {"class": "genre"})
    genre = genre[0].text.strip()

    try:
        rating = container.div.div.findAll("span", {"class": "ipl-rating-star__rating"})
        rating = rating[0].text
    except:
        rating = "N/A"

    try:  
        metascore = container.findAll("div", {"class": "inline-block ratings-metascore"})
        metascore = metascore[0].span.text.strip()
    except:
        metascore = "N/A"

    f.write(title.replace(",", "|") + "," + year + "," + age_rating + "," + lenght + "," + genre.replace(",", " |") + "," + rating + "," + metascore + "\n")

f.close()