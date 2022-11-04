from bs4 import BeautifulSoup, NavigableString, Tag
import requests as r
import asyncio
import pandas as pd
import numpy as np

def scrape_server():
    url = "Google Sheet URL"

    res = r.request('GET', url).content

    soup = BeautifulSoup(res, 'html.parser')

    items = []

    for item in soup.findAll("td", recursive=True):
        for string in item.stripped_strings:
            if(string != "Tag" and string != "NEW"):
                items.append(string)

    columns = 6
    rows = int(len(items) / columns)
    items = np.array(items).reshape(rows, columns)

    df = pd.DataFrame(items[1:,:], columns=items[0,:])
    df = df.set_index("ID")

    df.to_csv("v2ray.csv")

    return open('v2ray.csv', 'rb')