#jdParser 2.0
import urllib2
from bs4 import BeautifulSoup
import re
POSITIVE=re.compile("article|body|hentry|main|content|job",re.I)
NEGATIVE=re.compile("header|head|foot|footer|footerMenu|footmenu|meta|sponsor|sidebar|comment|contact",re.I)

url = raw_input("Enter a  Url : ")
urlopen=urllib2.urlopen(url)
soup=BeautifulSoup(urlopen,'html.parser')

for x in soup.find_all("script"):
    x.extract()
for x in soup.find_all("style"):
    x.extract()
for x in soup.find_all("link"):
    x.extract()
for x in soup.find_all("img"):
    x.extract()

candidates=[]

allParas=soup.find_all("p")



for paras in allParas:
    #print type(paras)
    candidate = paras
    
    if candidate not in candidates:
        candidates.append(candidate)
        candidate.clear()
        candidate.score=0
        if "class" in candidate:
            if NEGATIVE.match(candidate["class"]):
                candidate.score-=50
            if POSITIVE.match(candidate["class"]):
                candidate.score-=50
        if "id" in candidate:
            if NEGATIVE.match(candidate["id"]):
                candidate.score-=50
            if POSITIVE.match(candidate["id"]):
                candidate.score-=50        
    if candidate.score is None :
        candidate.score=0
       
for x in candidates:
    print x.score
    print x
    
