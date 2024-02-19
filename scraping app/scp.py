import requests
from bs4 import BeautifulSoup as bs
import gspread
import time

# google sheets API
gc = gspread.service_account(filename="credentials.json")
sh = gc.open_by_key('1CPkUwhGGZZFbTlOZKavGStC_5L0iJlCcVq2fuC7HZTw')
worksheet = sh.sheet1

 #booklist
booklist=[]



 #scraping from goodreads for loop 100 pages
 #https://www.goodreads.com/shelf/show/thriller?page=1-100
start_url= "https://www.goodreads.com"
sec_url= "/shelf/show/thriller?page="
html_code= ".html"

for i in range(2,4):
    page_num = str(i)
    page = requests.get(start_url+sec_url+str(2)+html_code)
    soup = bs(page.content, 'html.parser')
    print(start_url+sec_url+page_num+html_code)



    #data collection
    titles = soup.find_all('a', class_='bookTitle')
    authors = soup.find_all('a', class_='authorName')
    ratings = soup.find_all('span', class_='greyText smallText')


    #loop to scrap title author rating and input  to sheets google drive
    for title, author, rating in zip(titles, authors, ratings):
        book_T= title.get_text()
        book_A= author.get_text()
        rating_var=rating.get_text()
        book_R = rating_var.split()[4].replace(",","")

        booklist=[book_T,book_A,int(book_R)]


        worksheet.append_row(booklist)



        print("one book done")
    time.sleep(2)
    print("------------------------------------------------------")
    print("one page done")
    print("------------------------------------------------------")

#project_href = [i['href'] for i in soup.find_all('a', class_='bookTitle', href=True)]
#print(project_href)
    #print("-----------------------------------------------------------------------------|")
#print(bookdic)
#print([int(x) for x in num])
#print(sorted([int(x) for x in num], reverse = True))

#book=["huba","ihab",20232]

#res = worksheet.get()
#print(res)
#worksheet.insert_row(book,2)
