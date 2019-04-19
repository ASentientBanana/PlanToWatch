#from jikanpy import Jikan
#jinkan = Jikan()
import requests , json
from bs4 import BeautifulSoup as soup 

inp = 'one piece'

def Lformat(inp):
    m = []
    for i in inp :
        if str(i) == " ":
            m.append('\\')
        else:
            m.append(i)
            
    return "".join(m).lower()

api_base = 'https://api.jikan.moe/v3/search/anime?q='+Lformat(inp) +'&page=1'


request = requests.get(api_base)

response = json.loads(request.text)
for i in response['results']:
    print(i['title'])
    print(i['episodes'])
    print(i['type'])
    break



print(api_base)

