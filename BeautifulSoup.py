

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

mywebpage = urlopen("http://www.kean.edu")

myWebpageContents = BeautifulSoup(mywebpage.read(), "html5lib");

# Display the Title of the webpage
print("The title of the webpage is:")
print(myWebpageContents.title)
print()

# Display all of the headings in the webpage
print("The h3 headings in the webpage are:")
tags = myWebpageContents.findAll("h3")
for i in tags:
	print(i.getText())
print()
print("The h2 headings in the webpage are:")
tags = myWebpageContents.findAll("h2")
for i in tags:
	print(i.getText())
print()
#Display all hyperlinks in the webpage
print("The webpage includes the following links:")
for link in myWebpageContents.findAll('a', attrs={'href': re.compile("^http://")}):
	print(link.get('href'))
print()
