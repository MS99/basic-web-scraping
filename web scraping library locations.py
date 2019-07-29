
# coding: utf-8

# In[3]:


# import libraries
import sys
from bs4 import BeautifulSoup


# In[4]:


# Determine which urllib library to use
if sys.version_info[0] < 3:
    from urllib2 import urlopen
else:
    from urllib.request import urlopen


# In[5]:


# Use the exact URL you want to scrape
locations = 'http://library.austintexas.gov/locations'


# In[6]:


# Use urllib2 or urllib to pull the html to the variable 'site'
site = urlopen(locations)


# In[7]:


# Parse the site
soup = BeautifulSoup(site, 'html.parser')


# In[18]:


# Retrieve data
all_locations = soup.find_all('div', attrs = {"apl-box"})


# In[24]:


for loc in all_locations [1:]:
    print(loc.find('h2', attrs = 'pane-title').text )

