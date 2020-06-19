# @author: Şükrü Erdem Gök https://github.com/SukruGokk
# @date: 19/06/2020
# @os: Windows 10 Python 3.8

# Simple link collector with python

# Lib
from bs4 import BeautifulSoup
from requests import get
from webbrowser import open
from sys import exit

# Get link from user with input
url = input("link(with https:// or http://):\n")

try:r = get(url)
except:
    input("ERROR")
    exit(0)

soup = BeautifulSoup(r.content, "lxml")

links = []

# Get links from site content
for link in soup.findAll('a'):
    # If it doesnt contains http, dont but if it contains append
    if str(link.get('href')).find("http") == -1:
        pass
    else:
        links.append(link.get('href'))

# Print them
for i in range(len(links)):
    print("{}. Link {}".format(i, links[i]))

# Get keyword that link must contain
key = input("Whick keyword should link contain:\n")
filtered = []

# Filter the links
for current in links:
    if current.find(key.lower()) != -1:
       filtered.append(current)

# Print them
for a in filtered:
    print("{}.{}".format(filtered.index(a), a))

try:
    number = int(input("Which link do you want to open (write number that at the beginning of the line)?:\n"))
except:
    input("ERROR")
    exit(0)

# Open the link
open(filtered[number])