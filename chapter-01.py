
# coding: utf-8

# # Web scraping com Python - Ch01

# In[1]:

from urllib.request import urlopen


# In[2]:

URL1 = 'http://pythonscraping.com/pages/page1.html'


# ## O método simples

# In[3]:

html = urlopen(URL1)
print(html.read())


# ## Tratando erros e usando o BeautifulSoup

# In[4]:

from bs4 import BeautifulSoup


# In[5]:

def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        soup = BeautifulSoup(html.read(), 'html.parser')
        title = soup.body.h1
    except AttributeError as e:
        return None
    return title

title = get_title(URL1)
if title == None:
    print('Título não encontrado')
else:
    print(title)

