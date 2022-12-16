import requests
from bs4 import BeautifulSoup
import csv

# Make an HTTP request to the website
response = requests.get('http://www.example.com')

# Parse the HTML or XML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the data you need using BeautifulSoup methods
items = soup.find_all('div', class_='item')

# Open a CSV file for writing
with open('items.csv', 'w', newline='') as csvfile:
  # Create a CSV writer object
  writer = csv.writer(csvfile)
  
  # Write the header row
  writer.writerow(['Name', 'Price'])
  
  # Write the data rows
  for item in items:
    name = item.find('h3').text
    price = item.find('span', class_='price').text
    writer.writerow([name, price])
