
pagenum = 0;
page=100;
var= "https://www.goodreads.com/shelf/show/thriller?page="
for pagenum in range(100):
    print(var + str(pagenum+1))
