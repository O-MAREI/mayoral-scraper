# File for testing and dev work. Finished pieces of code are moved to mayoral_scraper.py
import requests
from bs4 import BeautifulSoup
import re
baseurl = 'https://ballotpedia.org'
headers = {
    'User Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

# Gennerating the candidate links file.
""" 
with open("electionLinks.txt") as file:
    electionLinks = file.read().splitlines()

candidateLinks = []

for link in electionLinks:
    r2 = requests.get(link)
    soup = BeautifulSoup(r2.content, 'lxml')

    currentCandidates = soup.find_all("td", class_ = "votebox-results-cell--text")
    
    for i in range(len(currentCandidates)) :
        currentCandidates[i] = currentCandidates[i].find("a")
        if currentCandidates[i] != None:
            currentCandidates[i] = currentCandidates[i]["href"]
    
    if len(currentCandidates) != 0:
        currentCandidates = [x for x in currentCandidates if x]
        candidateLinks.append(currentCandidates)

for links in candidateLinks:
    for link in links:
        if link == None:
            del link
        else:
            print(link)
    print("-")
"""
with open("electionLinks.txt") as file:
    electionLinks = file.read().splitlines()


