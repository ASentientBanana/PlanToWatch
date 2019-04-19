import requests , json
from bs4 import BeautifulSoup 
url = "http://epguides.com/"
NURL = url + 'arrow'


request = requests.get(NURL)

soup = BeautifulSoup(request.text, 'html.parser')

title = soup.h1
print('Title: ',title)
filt = soup.find_all('tr',{'class':'center'})
print(filt)
lis = []
data_lis = []
dl = []

for i in filt:
    print(i)
    lis.append(i)


print(lis)
inf = lis[1]

for j in inf:
    data_lis.append(j)
i_1 = data_lis[7]#----runtime
i_2 = data_lis[3]#----episode count
i_3 = data_lis[9]#---- Genre

print('Number of episodes: ',i_2.string)
print('Episode Runtime: ',i_1.string)

for f in i_3:
    dl.append(f)


print('Genre: ',dl)
