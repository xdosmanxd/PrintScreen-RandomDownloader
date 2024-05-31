import requests
from bs4 import BeautifulSoup
import subprocess
import concurrent.futures
from random import shuffle
import os

letters = "abcdefghijklmnopqrstuwxyz"
liste = []

for first in letters:
	for second in letters:
		for number in range(1000,10000):
			liste.append("https://prnt.sc/" + first + second + str(number))

shuffle(liste)
print("Finished the list")

def image_saver(url):
	r = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"})
	soup = BeautifulSoup(r.text, features="lxml")
	source = soup.find("img").get("src")

	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
				'Accept-Encoding': 'none',
				'Accept-Language': 'en-US,en;q=0.8',
				'Connection': 'keep-alive'}

	file_ext = "." + source.split(".")[-1]
	file_name = url.split("/")[-1] + file_ext

	if source.startswith("https://image.prntscr.com"):

		r = requests.get(source, headers=hdr)
		if r.status_code != 404:
			with open(f"images/{file_name}", "wb") as file:
				file.write(r.content)
			print(f"Downloaded {file_name}")	

		else:
			print(f"İmage was removed(1) {url}")

	elif source.startswith("https://i.imgur.com"):
		command = ["curl", "-s", source, "-o", f"images/{file_name}"]
		subprocess.run(command)
		print(f"Downloaded {file_name}")
		
	elif source == ("//st.prntscr.com/2023/07/24/0635/img/0_173a7b_211be8ff.png"):
		print(f"İmage was removed(2) {url}")
		
	else:
		print(f"Couldn't identify the source skipping {url}")
		print(source)

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
	executor.map(image_saver, liste) 
