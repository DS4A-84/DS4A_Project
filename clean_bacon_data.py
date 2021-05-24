#!/usr/bin/python

# DS4A Project
# Group 84
# Clean Oracle of Bacon Json Blob data

file1 = open('data/bacon.txt', 'r', encoding="utf8")
Lines = file1.readlines()


blob_format_dict = {
    "INFOBOX: ":"",
    "=>":":",
    "[[": "",
    "]]":""
}



for i in Lines:
    i = for o, r in blob_format_dict.items():
        i = i.replace(o, r)


    print(i)
    exit()
