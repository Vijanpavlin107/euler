#moja resitev

#scrapanje iz weba
import requests
from bs4 import BeautifulSoup
from math import sqrt, prod
import re

url = "https://projecteuler.net/problem=11"
response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")
text = soup.get_text()
numbers = re.findall(r"\d+", text)

stevilo = soup.find("p", class_="monospace center")
raw = stevilo.get_text()
rows = raw.strip().split("\n")
grid = []
for row in rows:
    nums = [int(n) for n in row.split()]
    grid.append(nums)



#resevanje naloge
#input mora biti seznam seznamov - matrika
def max_prod_4(mat):
    max_prod = 0
    dimenzija = int(sqrt(len(mat) * len(mat[0])))
    for vrstica in mat:
        for i in range(0, dimenzija - 4):
            produkt = prod([vrstica[j] for j in range(i, i + 4)])
            max_prod = produkt if produkt > max_prod else max_prod
        
        for k in range(0, dimenzija-4):
            for l in range(0, dimenzija-4):
                produkt = prod([mat[h,k] for h in range(l,l+4)])
                max_prod = produkt if produkt > max_prod else max_prod

    print(max_prod)

max_prod_4(grid)
    
    



