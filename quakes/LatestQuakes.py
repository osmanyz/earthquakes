from urllib.request import urlopen
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup
import re


class LatestQuakes:
    """
    Son Depremlerin Listesi
    """
    PATH = 'http://m.koeri.boun.edu.tr/dbs/deprem-listesi-touch.asp?sort=tarih&sira=desc&kull_lat=&kull_lon='

    def __init__(self, path=None):
        self.PATH = path if path is not None else self.PATH

    def reader(self):
        html_reader = urlopen(self.PATH)
        return BeautifulSoup(html_reader, "html.parser")

    @staticmethod
    def url_parser(url):
        url_parse = urlparse(url).query
        return parse_qs(url_parse)

    @staticmethod
    def href_replace(href):
        return href.get('onclick').replace("window.top.location.href='", "").replace("';", "")

    @staticmethod
    def name_replace(name):
        return name.select_one(".namediv").text.replace(" ", "").replace('\n', "")

    @staticmethod
    def date_replace(date_value):
        date = date_value.select_one(".tarihdiv").text.replace(' ', "")

        deep = re.search(r'(\d+.*\d+)km', date).group(1)
        time = re.search(r'(\d+/\d+/\d+)', date).group(1)
        hours = re.search(r'(\d+:\d+:\d+)', date).group(1)

        return {'deep': deep, 'time': time, 'hours': hours}

    def latest_quakes(self):
        results = []
        readers = self.reader(self).select('table > tr')

        for item in readers:
            ml = item.find("div")
            href = self.href_replace(ml)

            parse = self.url_parser(href)
            lat = parse['lat']
            lon = parse['lon']

            name = self.name_replace(item)
            date = self.date_replace(item)

            results.append({'href': href,
                            'text': ml.text,
                            'lat': lat,
                            'lon': lon,
                            'name': name,
                            'deep': date['deep'],
                            'time': date['time'],
                            'hours': date['hours'],
                            })

        return results

    @staticmethod
    def work():
        return LatestQuakes.latest_quakes(LatestQuakes)


if __name__ == '__main__':
    quake = LatestQuakes()
    quake.work()

