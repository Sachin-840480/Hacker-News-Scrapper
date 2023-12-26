#Hacker News Scrapper.

#Implement a way to also scrape the 2nd Page of the Hacker News as well. As this script only does for 1st Page.

##We can create a function to loop through the links, a certain number of times the user specifies.
''' Example Code '''

# for link in links:
#     result = requests.get(f'{root}/{link}')
#     content = result.text
#     soup = BeautifulSoup(content, 'html.parser')

#---------------------------------------------#

import requests
from bs4 import BeautifulSoup
from pprint import pprint

'''---------------------------------------------------'''

#The 1st Page Object.
res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')


#The 2nd Page Object.
res2 = requests.get('https://news.ycombinator.com/?p=2')
soup2 = BeautifulSoup(res2.text, 'html.parser')

'''---------------------------------------------------'''

# Selecting 'links' and 'text' from the 1st Page.
links = soup.select('.titleline > a') 
subtext = soup.select('.subtext')


# Selecting 'links' and 'text' from the 2nd Page.
links2 = soup.select('.titleline > a')  
subtext2 = soup2.select('.subtext')

'''---------------------------------------------------'''

#Combining all the 'links' and 'subtexts', to make a larger 'link' and 'subtext'.
mega_link = links + links2
mega_subtext = subtext + subtext2


'''---------------------------------------------------------------------------------'''


#Creating a Function to sort the stories based on the votes.

def sort_stories_by_votes(hn_list):
    return sorted(hn_list, key = lambda k: k['votes'], reverse = True)      # We get all the Stories in Descending Order.


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


# pprint(create_custom_hn(links, subtext))    #Calling the Create_custome_hn() function.

#We change the 'passing parameter' with the new 'links' and 'subtexts' to "mega_link" and "mega_subtext".

pprint(create_custom_hn(mega_link, mega_subtext))    #Calling the Create_custome_hn() function.