import requests
from bs4 import BeautifulSoup as bs
import gspread

# google sheets API
gc = gspread.service_account(filename="credentials.json")
sh = gc.open_by_key('1CPkUwhGGZZFbTlOZKavGStC_5L0iJlCcVq2fuC7HZTw')
worksheet = sh.sheet1
# scraping from goodreads
#url= "https://www.goodreads.com/shelf/show/thriller"
#page = requests.get(url)
#soup = bs(page.content, 'html.parser')
#bookdic ={}

#titles = soup.find_all('a', class_='bookTitle')
#authors = soup.find_all('a', class_='authorName')
#ratings = soup.find_all('span', class_='greyText smallText')
#    for title, author, rating ,in zip(titles, authors, ratings):
#    bookdic["title"] = title.get_text()
#    bookdic["author"]  = author.get_text()
#    rating_var  =rating.get_text()
#    bookdic["rating"] = rating_var.split()[4].replace(",","")
#    worksheet.append_row(title)
#    worksheet.append_row(author)
#    worksheet.append_row(rating)


#    print("done")

    #print("-----------------------------------------------------------------------------|")
#print(bookdic)
#print([int(x) for x in num])
#print(sorted([int(x) for x in num], reverse = True))

#book=["huba","ihab",20232]

res = worksheet.get('A1')
print(res)
#worksheet.insert_row(book,2)
