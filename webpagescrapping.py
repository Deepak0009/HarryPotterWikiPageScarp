import re
import os
import csv
import time
import lxml
import requests
import pymongo
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


def output_file(name):
    try:
        csv_directory = os.getcwd()
        csv_filename = name + '_' + str(round(time.time() * 1000)) + ".csv"
        path = csv_directory + "\\" + csv_filename
        if os.path.isdir(csv_directory):
            print("")
    except FileNotFoundError as e:
        raise e
    return path


def write_csv(url):
    name = ''.join(re.findall(r"(?<=wiki\/)\w+", url))
    filename = output_file(name)
    with open(filename, 'w', encoding='UTF-8') as outfile:
        writer = csv.writer(outfile)
        headers = ["word", "count"]
        writer.writerow(headers)
        words = Counter(line.strip().lower() for lines in parse_html(url) for line in lines.split())
        for key, value in words.items():
            writer.writerow([key, value])

write_csv('provide your wiki url here')