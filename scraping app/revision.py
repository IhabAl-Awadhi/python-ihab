import requests
from bs4 import BeautifulSoup as bs
import time

linelist=[]
# file for data collection
f= open("Q&A.txt","a")

#https://doc.xuehai.net/b94d214d9d502aafdd909bb14e10b5153e395a490-21.html
 #https://www.goodreads.com/shelf/show/thriller?page=1-100
start_url= "https://doc.xuehai.net"
sec_url= "/b94d214d9d502aafdd909bb14e10b5153e395a490-"
html_code= ".html"

for i in range(1,10):
    page_num = str(i)
    page = requests.get(start_url+sec_url+page_num+html_code)
    soup = bs(page.content, 'html.parser')
    print(soup)



    #data collection
    QA = soup.find_all('p')




    #loop to scrap title author rating and input  to sheets google drive
    for qa in zip(QA):
        quastion_answer= qa.get_text()
        linelist=[quastion_answer]
        print(linelist)
        f.write(str(linelist)+"\n")



    print("page done")
    time.sleep(3)




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
