#!/usr/bin/python

# DS4A Project
# Group 84
# Clean Oracle of Bacon Json Blob data


# Import Python Modules
from functools import reduce
from get_bacon_kaggle_conflict_names.py import categories_interest



# Data
bacon_data_path = 'data/bacon.txt'
kaggle_data_path = 'data/the_oscar_award_corrected.csv'
categories_interest
print(categories_interest)
exit()

def load_txt_data(filepath):
    '''
    Inputs: filepath - str path to input data

    input data is in a txt file

    returns: output data is a readlines object
             of the text file
    '''

    a = open(filepath, 'r', encoding="utf8")
    return a.readlines()


def load_csv_data(filepath):
    '''
    Inputs: filepath - str path to input data

    input data is in a csv file

    returns: pandas dataframe of file contents
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
    for i in lines:
        if '{"title' in i :
            i = reduce(lambda x, y: x.replace(y, dict[y]), dict, i)
            result.append(i)

    return result



raw_bacon_data = load_txt_data(bacon_data_path)
clean_bacon_data = write_clean_blob_to_txt(raw_bacon_data,output_path)
print(len(clean_bacon_data))
print(clean_bacon_data[40][1])
