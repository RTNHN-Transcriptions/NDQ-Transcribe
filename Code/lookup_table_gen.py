import whisper #pip install openai-whisper
from bs4 import BeautifulSoup as Soup #pip install bs4 lxml
import requests #pip install requests - Not actually sure if you need to install this manually
from os.path import exists
from tqdm import tqdm #pip install tqdm
import json
import torch


# RSS_LINK = "https://thetenminutebiblehourpodcast.libsyn.com/rss"
# RSS_doc = requests.get(RSS_LINK)
# soup = Soup(RSS_doc.content, features="xml")
# episodes = soup.find_all("item")
# lookup_table = {}

# for episode in episodes:
#     title = episode.title.text
#     episode_number = title[:title.find("-")-1]
#     lookup_table[episode_number] = episode_number

with open("lookup_table.json", "r") as f:
    lookup_table = json.load(f)

for i in range(41, 201):
    str(i).zfill(3)  
    lookup_table[f"EST{str(i).zfill(3) }"] = f"EST{str(i).zfill(3) }"

with open("lookup_table.json", "w+") as f:
    json.dump(lookup_table, f)

# with open("lookup_table.json", "w+") as f:
#     json.dump(lookup_table, f)