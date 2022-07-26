import re
import csv
import lxml
import requests
from bs4 import BeautifulSoup
from collections import Counter


def get_html(url):
    try:
        response = requests.get(url)
        return response
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


def parse_html(url):
    page = get_html(url).content
    soup = BeautifulSoup(page, "lxml")
    paragraphs = soup.findAll('p')
    paragrpah_lines = (''.join(re.sub(r"[0-9]+|\.|\,|\:|\/|\-|\$|\?|\[|\]|\%|\"|\(|\)|\'|\;|&|^\s|\b[a-zA-Z]\b",
                    '', para.text.strip())) for para in paragraphs)
    return paragrpah_lines


def write_csv(url):
    with open("harry.csv", 'w', encoding='UTF-8') as outfile:
        writer = csv.writer(outfile)
        headers = ["word", "count"]
        writer.writerow(headers)
        words = Counter(line.strip().lower() for lines in parse_html(url) for line in lines.split())
        for key, value in words.items():
            writer.writerow([key, value])


write_csv(url="https://en.wikipedia.org/wiki/Harry_Potter")