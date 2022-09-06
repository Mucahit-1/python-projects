from bs4 import BeautifulSoup
import requests

url ="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)

website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
all_moves = soup.find_all(name="h3" , class_="title")

moves_title =  [title.getText() for title in all_moves]
moves = moves_title[::-1]

with open("moves.txt" , mode="w" , encoding="utf8") as file:
    for move in moves:
        file.write(f"{move}\n")
