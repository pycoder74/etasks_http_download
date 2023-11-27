from bs4 import BeautifulSoup
import requests
import os
from nltk.tokenize import word_tokenize
os.system('pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org nltk')
url = 'https://github.com/pycoder74/eTasks'
ext = 'iso'

def listFD(url, ext=''):
    page = requests.get(url, verify = False).text
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
directories =listFD(url)
list = []
for i in directories:
    list.append(i)
    tokenized_input = word_tokenize(i)
    if 'blob' in tokenized_input[2]:
        print(tokenized_input[2])
    else:
        pass
    
    
