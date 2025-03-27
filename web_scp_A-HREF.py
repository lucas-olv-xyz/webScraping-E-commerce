import requests
from bs4 import BeautifulSoup
import csv

# Send an HTTP request to the web page
response = requests.get('https://wantedind.com/')

# Parse the HTML of the web page
soup = BeautifulSoup(response.text, 'html.parser')

# Find the data you want to extract
data = soup.find_all('href')

# Print the data to a csv file
with open('data.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['a'])
  
  for link in soup.find_all('a'):
    # data1 = item.find('box-image')
    # writer.writerow([data])
    data1 = link.get('href')
    writer.writerow([data1])