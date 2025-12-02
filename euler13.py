
import requests
from bs4 import BeautifulSoup

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
stevila_raw = nums.strip()
stevila_raw = stevila_raw.split("\n")
stevila_raw = stevila_raw[1:]
stevila = [int(i[:50]) for i in stevila_raw]

# print(len(stevila)) #tocni podatki

sestevek = sum(stevila)

print(str(sestevek)[:10]) #pravilno