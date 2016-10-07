
# coding: utf-8

# In[1]:

import requests
import html2text
import urllib2
import csv
import pandas as pd
import re

# URL to Text via Readability API

API_TOKEN = 'c798b3e0e6b0017ec35fed6b258c309eb2ca2956'

# GET /api/content/v1/parser?url=*URL*&token=*NUMBER*

base_url = 'https://readability.com'

def url_builder(target_url):
    return '%s/api/content/v1/parser?url=%s&token=%s' % (base_url, target_url, API_TOKEN)

#Retrevies JSON file

def get_content(target_url):
    try:
        target_url=url(target_url)
        if '+' in target_url:
            content='unable to read'
        else:
            resp = requests.get(url_builder(target_url))
            if 'content' in resp.json():
                html_content = resp.json()['content']
                content=html2text.html2text(html_content)
                content=alphanumeric(content)
                content=size(content)
            elif raw_page(target_url):
                content='double check'
            else:
                content='both fucked up'
    except:    
        content='all fucked up'
    return content

def alphanumeric(text):
    pattern = re.compile('\W')
    alpha = re.sub(pattern, ' ', text)
    return alpha

def size(content):
    if len(content) > 25000:
        content = 'more than twenty five thousand words'
    else:
        return content
    return content

def url(text):
    sep = '#'
    rest = text.split(sep, 1)[0]
    return rest

def short_text(df, search_term):
    short=[]
    shorter=[]
    q=re.compile(r'((?:\S+\s+){0,15})\b' + re.escape(search_term) + r'\b\s*((?:\S+\s+){0,15})')
    for text in df.text:
        try:
            result=q.findall(text.lower())
            shorty=[]
            for tupl in result:
                search_term=search_term.upper()
                tupl= search_term.join(tupl)
                shorty.append(tupl)
            short.append(shorty)
        except Exception as e:
            result='NO WORK %s' % e
            short.append(result)
    for snippet in short:
        snippet=' *** '.join(snippet)
        shorter.append(snippet)
    return shorter

def freq_count(item, text):
    text=text.lower()
    count=text.count(item)
    return count
    
    
def translated(text):
    'uses html2text.html2text to interrupt webpage'
    rawness=raw_page(text)
    translated=html2text.html2text(rawness)
    print (translated)
    
def raw_page(text):
    'Downloads a webpage and returns the text.'
    page = urllib2.urlopen(text)
    return page.read()
