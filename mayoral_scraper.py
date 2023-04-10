import requests
from bs4 import BeautifulSoup
import re
baseurl = 'https://ballotpedia.org'

# Changing the header to not arise suspicion from the website.
headers = {
    'User Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

# This section is for scraping all the links for mayoral elections.
r = requests.get('https://ballotpedia.org/United_States_municipal_elections,_2023')
soup = BeautifulSoup(r.content, 'lxml')

cityList = soup.find_all("a", string="Mayor")

electionLinks = []

for city in cityList:
    electionLinks.append(baseurl + city['href'])

electionsNumber = len(electionLinks)

#---------------------------------------------------------------

candidateLinks = []

for link in electionLinks:
    r2 = requests.get(link)
    soup = BeautifulSoup(r2.content, 'lxml')

    currentCandidates = soup.find_all("td", class_ = "votebox-results-cell--text")

    for i in range(len(currentCandidates)) :
        currentCandidates[i] = currentCandidates[i].find("a")
    
    currentCandidates = list(dict.fromkeys(currentCandidates))
    candidateLinks.append(currentCandidates)

isolatedLinks = []

for candidate in candidateLinks:
    isolatedLinks.append(baseurl + candidate['href'])
    print(baseurl + candidate['href'])