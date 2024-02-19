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

# file for data collection
f= open("book data.txt","a")



 #scraping from goodreads for loop 100 pages
 #https://www.goodreads.com/shelf/show/thriller?page=1-100
start_url= "https://www.goodreads.com"
sec_url= "/list/show/1.Best_Books_Ever?page="
html_code= ".html"

for i in range(1,4):
    page_num = str(i)
    page = requests.get(start_url+sec_url+page_num+html_code)
    soup = bs(page.content, 'html.parser')
    print(start_url+sec_url+page_num+html_code)



    #data collection
    titles = soup.find_all('a', class_='bookTitle')
    authors = soup.find_all('a', class_='authorName')
    ratings = soup.find_all('span', class_='minirating')
    nums = soup.find_all('td', class_='number')


    #loop to scrap title author rating and input  to sheets google drive
    for title, author, rating,num in zip(titles, authors, ratings,nums):
        book_T= title.get_text()
        book_A= author.get_text()
        rating_var=rating.get_text()
        book_R = rating_var.split()[4].replace(",","")
        num= num.get_text()

        booklist=[num,book_T,book_A,book_R]
        time.sleep(.2)
        f.write(str(booklist)+"\n")

        #worksheet.append_row(booklist)
        print("book #"+num+" Done")



    print("one book done")
    time.sleep(3)
    print("------------------------------------------------------")
    print("start page done")
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

#URLSTART="https://www.goodreads.com"
#BESTBOOKS="/list/show/1.Best_Books_Ever?page="

#start_url= "https://www.goodreads.com"
#sec_url= "/shelf/show/thriller?page="
#html_code= ".html"
