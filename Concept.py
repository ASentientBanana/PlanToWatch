import bs4 , urllib3 , json , requests
from jikanpy import Jikan
jikan = Jikan()


base_url = "https://api.jikan.moe/v3"

search_result = jikan.search('anime', 'Bleach', )


print(search_result)

#data  = json.loads(search_result)
#print(type(data))
