"""
# 
# File : L00169700_Q2_File_2.py
# Created ：24.11.21
# Author ：R.Lima
# Version ：v1.0.0
# Licencing : (C) 2021 R.Lima, LYIT
# Available under GNU Public License (GPL)
# Description ：Using Python on your host (windows) pc scrape the Apache 2 page
"""

from bs4 import BeautifulSoup
import requests # to get image from the web

user_agent = 'Chrome/80.0.3987.132 Mozilla/5.0'

url = "http://192.168.1.103/"

r = requests.get(url , headers={'User-Agent': user_agent})
soup = BeautifulSoup(r.text, 'html.parser')

#print (soup)

header = soup.find("head")
print ("header : ", header.text)

split_by_space = str(soup).split(" ")
#print (split_by_space[:10:])

apache2_word_appear_count = 0
for word in split_by_space:
    if (word.strip() == "Apache2"):
        apache2_word_appear_count += 1

print ("Number of times the word Apache2 Appears :", apache2_word_appear_count)

# Finding Section Headers

print ("Section Headers")
section_headers = soup.findAll("div",{"class":["section_header"]})

for section_header_index in range(len(section_headers)):
    section_header = section_headers[section_header_index].text.replace("\r","").replace("\n","").strip()
    print (section_header_index+1, ":", section_header)
