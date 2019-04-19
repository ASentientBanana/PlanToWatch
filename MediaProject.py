import requests , bs4 , json
from bs4 import BeautifulSoup as soup 
#from jikanpy import Jikan
#inkan = Jikan()

print("Hi! , What are you looking for?")
Start = input("A movie , show or anime: ")
c1 = input("Whats the title ")
    

# links used

Tv = "http://epguides.com"
Movie = "http://www.omdbapi.com/?i=tt3896198&apikey=7d668bae"
Anime = "https://www.anime-planet.com/anime/" # API used instead

# Just serches for the movie information with the IMDB API
def getmovieinfo(inp):
    mov = "http://www.omdbapi.com/?t=" +c1+ "&apikey=7d668bae"

    req = requests.get(mov)
    r = json.loads(req.text)
    t = r['Title']
    g = r["Genre"]
    ru = r["Runtime"]
    
    
    if inp == "title":
        return t
    elif inp == "genre":
        return g
    elif inp == "runtime":
        return ru
    #logic for the output






class MOVIE:
    def __init__(self,title,genre,runtime):
        self.title = title
        self.genre = genre
        self.runtime = runtime


class SHOW:
    def __init__(self,title,genre,episodes):
        self.title = title
        self.genre = genre
        self.episodes = episodes


class ANIME:
    def __init__(self,title,genre,episodes,):
        self.title = title
        self.genre = genre
        self.episodes = episodes


    
    


   





#-------------------------------TV Show-----------------------------------
def getTvinfo(inp):


    base_url = "http://epguides.com/"
    def concat(inp):
        ce = []
        for i in inp:
            if i != " ":
                ce.append(i)
        
        st = ''.join(ce)
        return st


    scrape_url = base_url + concat(c1)

    request = requests.get(scrape_url)
    formated = soup(request.text , 'html.parser')
    #print(formated)
    filt = formated.find_all('tr',{'class':'center'})
    lis = []
    data_lis = []
    dl = []
    for i in filt:
        #print(i)
        lis.append(i)
        



    inf = lis[1] #------- error list out of range
    
    for j in inf:
        data_lis.append(j)
    
    i_1 = data_lis[7]#----runtime
    i_2 = data_lis[3]#----episode count
    i_3 = data_lis[9]#---- Genre

    for f in i_3:
        dl.append(f)


    #print('Genre: ',dl)



    if inp == "runtime":
        return i_1.string
    elif inp == "episodes":
        return i_2.string
    elif inp == "Genre":
        return i_3






#--------------------------Anime----------------------------------
def getAnimeinfo(inp):
    

    def Lformat(inp):
        
        
        m = []
        for i in inp :
            if str(i) == " ":
                m.append('\\')
            else:
                m.append(i)
        #formats the input string        
        return "".join(m).lower()

    api_base = 'https://api.jikan.moe/v3/search/anime?q='+Lformat(c1) +'&page=1'
    request = requests.get(api_base)

    response = json.loads(request.text)
    
    for i in response['results']:
        t = i['title']
        e = i['episodes']
        ty = i['type']


        
        break

    if inp == "title":
        return t
    elif inp == "episodes":
        return e
    elif inp == "type":
        return ty





#-----------------------input logic------------------------------------
if Start == "movie":
    Mvar = getmovieinfo('title')
    Mvar2 = getmovieinfo('genre')
    Mvar3 = getmovieinfo('runtime')

    

    print('Title: ',Mvar)
    print("The Genre: ",Mvar2)
    print("The Runtime: ",Mvar3)

# Output for Movies

elif Start == "show":
    Svar0 = getTvinfo('runtime')
    Svar1 = getTvinfo('episodes')
    Svar2 = getTvinfo('Genre')
    
    print('runtime : ',Svar0)
    print("Number of episodes : ",Svar1)
    print("Genre : ",Svar2)


elif Start == "anime":
    Avar0 = getAnimeinfo('title')
    Avar1 = getAnimeinfo('episodes')
    Avar2 = getAnimeinfo('type')
    

    # Output for Anime

    print('Title: ',Avar0)
    print("Number of episodes : ",Avar1)
    print("Type : ",Avar2)
else:
    print("Invalide input")




