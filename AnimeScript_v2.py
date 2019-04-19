#from jikanpy import Jikan
#jinkan = Jikan()
#
#anime = jinkan.anime(456)
#print(anime['episodes'])
#print(anime['title'])

#def idCol():
#    
#    f = open('identification.txt',"w+")
##write
#    for i in range(1,10000):
#        anime = jinkan.anime(i)
#        f.write(anime["title"] + ':'+ str(i) +"\r\n")
#        print(f.write(anime["title"] + ':'+ str(i) +"\r\n"))
#
#
#
#
#idCol()
import requests
from bs4 import BeautifulSoup


Anime = "https://www.anime-planet.com/anime/"
st = 'Hunter x Hunter'
naziv = input("enter anime name: ")
def Lformat(naziv):
    m = []
    for i in naziv :
        if str(i) == " ":
            m.append('-')
        else:
            m.append(i)
            
    return "".join(m).lower()


aTitle =Lformat(naziv)
name = Anime+aTitle
request = requests.get(name)
soup = BeautifulSoup(request.text,'html.parser')

tags = soup.find('div',{'class':"tags"})
for i in tags:
    for k in i:
        print(k.string)

#------------works!------------------    
