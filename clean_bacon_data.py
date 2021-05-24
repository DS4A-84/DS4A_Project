#!/usr/bin/python

# DS4A Project
# Group 84
# Clean Oracle of Bacon Json Blob data

from functools import reduce


bacon_data_path = 'data/bacon.txt'
output_path = 'data/clean_bacon_dicts.txt'
def load_txt_data(filepath):
    a = open(filepath, 'r', encoding="utf8")
    return a.readlines()

def write_clean_blob_to_txt(lines,filepath):
    dict = {
        "INFOBOX: ":"",
        "=>":":",
        "[[": "",
        "]]":""
        }

    file = open(filepath,"a", encoding="utf8")
    for i in lines:
        if "INFOBOX:" in i  or '{"title' in i :
            file.write(reduce(lambda x, y: x.replace(y, dict[y]), dict, i))
    file.close()




#ff = load_txt_data(bacon_data_path)
#rr = write_clean_blob_to_txt(ff,output_path)

a = open(output_path,'r', encoding="utf8")
aa = a.readlines()
for i in aa:
    if "\n" in i:
        print(i)
