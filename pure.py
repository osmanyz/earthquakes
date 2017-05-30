from urllib.request import urlopen
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup

import re

page = urlopen("http://m.koeri.boun.edu.tr/dbs/deprem-listesi-touch.asp?sort=tarih&sira=desc&kull_lat=&kull_lon=")
read = BeautifulSoup(page, "html.parser")
data = []
count = 0

for item in read.select('table > tr'):
    # ml information
    ml = item.find("div")

    ml_href = ml.get('onclick')\
        .replace("window.top.location.href='", "")\
        .replace("';", "")

    ml_text = ml.text

    url_parse = urlparse(ml_href).query
    parse = parse_qs(url_parse)

    lat = parse['lat']
    lon = parse['lon']

    # location name
    name = item.select_one(".namediv")\
        .text.replace(" ", "")\
        .replace('\n', "")

    # date, hours, deep
    date = item.select_one(".tarihdiv")\
        .text.replace(' ', "")

    deep = re.search(r'(\d+.*\d+)km', date).group(1)
    time = re.search(r'(\d+/\d+/\d+)', date).group(1)
    hours = re.search(r'(\d+:\d+:\d+)', date).group(1)

    data.append({'ml_href': ml_href, 'ml_text': ml_text, 'lat': lat, 'lon': lon, 'name': name, 'deep': deep, 'time': time, 'hours': hours})
