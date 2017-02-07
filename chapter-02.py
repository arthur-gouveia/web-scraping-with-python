
# coding: utf-8

# # Web Scraping com Python - Ch02

# In[1]:

from urllib.request import urlopen

from bs4 import BeautifulSoup


# In[2]:

URL = 'http://www.pythonscraping.com/pages/warandpeace.html'

html = urlopen(URL)
soup = BeautifulSoup(html, 'html.parser')


# In[3]:

name_list = soup.find_all('span', {'class':'green'})
for name in name_list:
    print(name.get_text())


# In[6]:

# Buscando todos os headers de h1 a h6
soup.find_all({f'h{i}' for i in range(1, 7)})


# In[9]:

# Buscando tags que contenham o texto 'the prince'
len(soup.find_all(text='the prince'))


# In[10]:

# Assinatura de find_all: find_all(name, attrs, recursive, string, limit, **kwargs)
# Usando um atributo da tag
soup.find_all(id='text')
# Equivale a .find_all('', {'id': 'text'})


# In[13]:

soup.find_all('', {'class':'green'})


# ## Navegando na árvore HTML

# In[15]:

URL2 = 'http://www.pythonscraping.com/pages/page3.html'
html = urlopen(URL2)
soup = BeautifulSoup(html, 'html.parser')

