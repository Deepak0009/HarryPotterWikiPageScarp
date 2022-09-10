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


# def output_file(name):
#     try:
#         csv_directory = os.getcwd()
#         csv_filename = name + '_' + str(round(time.time() * 1000)) + ".csv"
#         path = csv_directory + "\\" + csv_filename
#         if os.path.isdir(csv_directory):
#             print("")
#     except FileNotFoundError as e:
#         raise e
#     return path


# def write_csv(url):
#     name = ''.join(re.findall(r"(?<=wiki\/)\w+", url))
#     filename = output_file(name)
#     with open(filename, 'w', encoding='UTF-8') as outfile:
#         writer = csv.writer(outfile)
#         headers = ["word", "count"]
#         writer.writerow(headers)
#         words = Counter(line.strip().lower() for lines in parse_html(url) for line in lines.split())
#         for key, value in words.items():
#             writer.writerow([key, value])


# def write_csv(url):
#     name = ''.join(re.findall(r"(?<=wiki\/)\w+", url))
#     filename = output_file(name)
#     with open(filename, 'w', encoding='UTF-8') as outfile:
#         writer = csv.writer(outfile)
#         headers = ["word", "count"]
#         writer.writerow(headers)
#         words = Counter(line.strip().lower() for lines in parse_html(url) for line in lines.split())
#         for key, value in words.items():
#             writer.writerow([key, value])

def save_to_mongo_cloud(url):
    #words = dict(Counter(line.strip().lower() for lines in parse_html(url) for line in lines.split()))
    # print(words)
    client = pymongo.MongoClient("mongodb+srv://dmishra1:Nov#2021@cluster0.wm8iquh.mongodb.net/?retryWrites=true&w=majority")
    # client = pymongo.MongoClient("mongodb://dmishra1:Nov#2021@ac-lx04lzm-shard-00-00.wm8iquh.mongodb.net:27017,ac-lx04lzm-shard-00-01.wm8iquh.mongodb.net:27017,ac-lx04lzm-shard-00-02.wm8iquh.mongodb.net:27017/?ssl=true&replicaSet=atlas-a3mq8v-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.db.sample_wiki
    db.insert_one({"_id":0, "user_name":"Soumi"})
    # if "wiki" in client.list_database_names():
    #     print("The database exists.")

    # col = db["words"]
    # if "data" in db.list_collection_names():
    #     print("The collection exists.")

    # try:
    #     col.insert_one({"_id":0, "user_name":"Soumi"})
    #     print('Inserted')
    # except:
    #     print('an error occured and data not stored')

# print(dict(Counter(line.strip().lower() for lines in parse_html("https://en.wikipedia.org/wiki/Ananya_Panday") for line in lines.split())))
save_to_mongo_cloud(url="https://en.wikipedia.org/wiki/Ananya_Panday")