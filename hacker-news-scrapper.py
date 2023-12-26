#Hacker News Scrapper.

import requests
from bs4 import BeautifulSoup
from pprint import pprint


res = requests.get('https://news.ycombinator.com/')         #1st Link.
soup = BeautifulSoup(res.text, 'html.parser')               #1st Object.
res2 = requests.get('https://news.ycombinator.com/?p=2')    #2nd Link.
soup2 = BeautifulSoup(res2.text, 'html.parser')             #2nd Object.


links = soup.select('.titleline > a')                       #1st Page.
subtext = soup.select('.subtext')                           #1st Page text.
links2 = soup2.select('.titleline > a')                     #2nd Page.
subtext2 = soup2.select('.subtext')                         #2nd Page text.


mega_link = links + links2                                  #Main 'Link'.
mega_subtext = subtext + subtext2                           #Main 'text'.


#Creating a Function to sort the stories based on the votes.
def sort_stories_by_votes(hn_list):
    return sorted(hn_list, key = lambda k: k['votes'], reverse = True)     


# Function to get the '{Title, links, votes}' of the 'Stories' with 'votes > 99'. 
def create_custom_hn(links, subtext):          
    hn = []                                  
    for idx, item in enumerate(links):
        title = item.getText()         
        href = item.get('href', None) 
        vote = subtext[idx].select('.score') 
        if len(vote):
            points = int(vote[0].getText().replace(' points', '')) 
            if points > 99:     
                hn.append({'title' : title, 'link' : href, 'votes' : points})     
    return sort_stories_by_votes(hn)        #Calling the "sort story by vote()" function.


pprint(create_custom_hn(mega_link, mega_subtext))    #Calling the Create_custome_hn() function.