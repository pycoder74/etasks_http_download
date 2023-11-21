from bs4 import BeautifulSoup
import requests

url = 'https://github.com/pycoder74/eTasks'
ext = 'iso'

def listFD(url, ext=''):
    page = requests.get(url, verify=False).text
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

directories = listFD(url)

needed_files = []
# Check for the presence of 'tree' in each directory
for directory in directories:
    if 'main' in directory and ".py" in directory:
        needed_files.append(directory)
    else:
        pass
print(f"Files to download: {needed_files}")
for i in needed_files:
    raw_url = i.replace('/tree/', '/raw/')
    response = requests.get(raw_url)
    print(f'Downloading file from {raw_url}')
    with open(f"{i.split('/')[-1]}", mode="wb") as file:
        file.write(response.content)
