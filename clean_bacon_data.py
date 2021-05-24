#!/usr/bin/python

# DS4A Project
# Group 84
# Clean Oracle of Bacon Json Blob data



# Import Python Modules
from functools import reduce


# Assign path variables for input, output
bacon_data_path = 'data/bacon.txt'
output_path = 'data/clean_bacon_dicts.txt'



def load_txt_data(filepath):
    '''
    Inputs: filepath - str path to input data

    input data is in a txt file

    returns: output data is a readlines object
             of the text file
    '''

    a = open(filepath, 'r', encoding="utf8")
    return a.readlines()


def write_clean_blob_to_txt(lines,filepath):
    '''
    Input: lines - readlines object
           filepath - str of output path

    Takes lines input and formats it to a python dictionary
    only keeps lines that are json blobs

    returns: nested list of dictionaries, a sub list is one movie
    '''

    dict = {
        "INFOBOX: ":"",
        "=>":":",
        "[[": "",
        "]]":"",
        "\n":""
        }


    result = []
    temp = []
    for i in lines:
        if '{"title' in i :
            i = reduce(lambda x, y: x.replace(y, dict[y]), dict, i)
            temp.append(i)
        if len(temp) == 2:
            result.append(temp)
            temp = []

    return result




raw_bacon_data = load_txt_data(bacon_data_path)
clean_bacon_data = write_clean_blob_to_txt(raw_bacon_data,output_path)
print(len(clean_bacon_data))
print(clean_bacon_data[40][1])
