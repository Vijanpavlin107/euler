

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
    vrstice = len(mat)
    stolpci = len(mat[0])

    #Horizontal
    for r in range(vrstice):
        for i in range(stolpci - 3):
            produkt = prod(mat[r][i:i+4])
            max_prod = max(max_prod, produkt)
    
    #Vertical
    for s in range(vrstice - 3):
        for r in range(stolpci):
            produkt = prod(mat[s+i][r] for i in range(4))
            max_prod = max(max_prod, produkt)

    #Diagonalno L-D
    for s in range(stolpci - 3):
        for r in range(vrstice - 3):
            produkt = prod(mat[s+i][r+i] for i in range(4))
            max_prod = max(max_prod, produkt)


    #Diagonalno D-L
    for s in range(3,stolpci):
        for r in range(vrstice-3):
            produkt = prod(mat[r+i][s-i] for i in range(4))
            max_prod = max(produkt, max_prod)

    print(max_prod)

max_prod_4(grid)
    
    



