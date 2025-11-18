#moja resitev
import requests
from bs4 import BeautifulSoup
from math import sqrt

url = "https://projecteuler.net/problem=11"
response = requests.get(url)





def max_prod_4(mat):
    seznam = [int(d) for d in str(mat)]
    dimenzija = int(sqrt(len(mat)))
    horizontal = [seznam[i:(i+dimenzija)] for i in range(0, len(seznam), dimenzija)]
    print(horizontal)

stevilke = 0


