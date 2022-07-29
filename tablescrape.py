from time import sleep
from turtle import heading
import requests
from bs4 import BeautifulSoup
import json

url = "https://www.centralbank.go.ke/tenders/"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')


table = soup.find("table", id="table_1" )


table_column = [ heading.text for heading in table.find_all("th")]

table_row = [ row for row in table.find_all("tr")]



results = [{table_column[index]:cell.text for index,cell in enumerate(row.find_all("td")) } for row in table_row]
print(results)



with open("tablescape.json", "w") as f:
    json.dump(results, f )
