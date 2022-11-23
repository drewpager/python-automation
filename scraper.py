import requests  
from bs4 import BeautifulSoup                          

response = requests.get("https://www.bbc.com/news")                                                       
soup = BeautifulSoup(response.content, "html.parser") 

print(soup.find_all("h2"))