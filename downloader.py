from bs4 import BeautifulSoup
import requests
import os

url = 'https://github.com/pycoder74/eTasks'
base_raw_url = 'https://raw.githubusercontent.com'

def listFD(url, ext=''):
    page = requests.get(url, verify=False).text
    soup = BeautifulSoup(page, 'html.parser')
    return [base_raw_url + url.replace('https://github.com', '') + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

directories = listFD(url, ext='.py')

needed_files = []

# Check for the presence of '.py' in each directory
for directory in directories:
    needed_files.append(directory)

print(f"Files to download: {needed_files}")

# Download files
for file_url in needed_files:
    response = requests.get(file_url)
    
    if response.status_code == 200:
        # Generate a unique filename with a timestamp
        filename = os.path.basename(file_url)
        print(f'Downloading file from {file_url}')
        with open(filename, mode="wb") as file:
            file.write(response.content)
    else:
        print(f'Failed to download file from {file_url}. Status code: {response.status_code}')
