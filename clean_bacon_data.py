#!/usr/bin/python

# DS4A Project
# Group 84
# Clean Oracle of Bacon Json Blob data

from functools import reduce


bacon_data_path = 'data/bacon.txt'
def load_txt_data(filepath):
    a = open(filepath, 'r', encoding="utf8")
    return a.readlines()

def movie_blob_to_dict(Lines):
    dict = {
        "INFOBOX: ":"",
        "=>":":",
        "[[": "",
        "]]":""
        }

    for i in Lines:
        i = reduce(lambda x, y: x.replace(y, dict[y]), dict, i)
        print(i)
        exit()

ff = load_txt_data(bacon_data_path)
rr = movie_blob_to_dict(ff)
