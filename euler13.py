from tkinter import Y
import requests
from bs4 import BeautifulSoup
import soupsieve

url = "https://projecteuler.net/problem=13"

# 1. Download HTML
resp = requests.get(url)
html = resp.text

soup = BeautifulSoup(html, "html.parser")

nums = soup.select_one("div.monospace.center")

# if nums is None:
#     print("not found")
# else:
#     print(nums.get_text)

nums = str(nums)
stevila = nums.strip()
stevila = stevila.split("\n")
stevila = stevila[1:]

print(stevila)


