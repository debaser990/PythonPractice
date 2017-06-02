from bs4 import BeautifulSoup
import urllib2
wiki_page='https://en.wikipedia.org/wiki/Animal-made_art'
page=urllib2.urlopen(wiki_page)
wikiSoup=BeautifulSoup(page,'html.parser')
footerbox=wikiSoup.find('div',attrs={'id':'footer'})
footertext=footerbox.text.strip()
print footertext
