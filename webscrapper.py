import requests
from bs4 import BeautifulSoup
import csv

# Make an HTTP request to the website
response = requests.get('http://example.com/')

# Parse the HTML or XML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the data you need using BeautifulSoup methods
data = soup.find_all('h1', 'p')

# Open a CSV file for writing
with open('data.csv', 'w', newline='') as csvfile:
  # Create a CSV writer object
  writer = csv.writer(csvfile)
  
  # Write the header row
  writer.writerow(['data1', 'data2'])
  
  # Write the data rows
  for item in data:
    data1 = item.find('h1')
    data2 = item.find('p')
    writer.writerow([data1, data2])
