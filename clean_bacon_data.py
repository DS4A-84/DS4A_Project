#!/usr/bin/python

# DS4A Project
# Group 84
# Clean Oracle of Bacon Json Blob data


# Import Python Modules
from functools import reduce
import pandas as pd
import json


# Data
bacon_data_path = 'data/bacon.txt'
corrected_kaggle_data_path = 'data/the_oscar_award_corrected.csv'
categories_interest = ['ACTOR',
                       'ACTRESS',
                       'ACTOR IN A LEADING ROLE',
                       'ACTRESS IN A LEADING ROLE',
                       'ACTOR IN A SUPPORTING ROLE',
                       'ACTRESS IN A SUPPORTING ROLE',
                       'DIRECTING',
                       'DIRECTING (Comedy Picture)',
                       'DIRECTING (Dramatic Picture)']


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

    df = pd.read_csv(filepath)
    return df


def blob_to_list(lines):
    '''
    Input: lines - readlines object
           filepath - str of output path

    Takes lines input and formats it to a python dictionary
    only keeps lines that are json blobs

    returns:  list of dictionaries formatted strings
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
        if 'INFOBOX' in i or '{"title' in i :

            #check for directors, year in line
            if 'directors' in i and 'year' in i:
                # clean the line
                i = reduce(lambda x, y: x.replace(y, dict[y]), dict, i)
                i = json.loads(i)
                result.append(i)

    return result

def create_info_title_pair_list(list):
    '''
    inputs -  list of strings in dictionary format

    takes in  list
    infobox and title adds sequential
    pairs to output list

    returns: a list of correctly sequential
    movie info/title movie dictionaies
    '''

    result = []
    temp = []

    for f in list:

        if len(temp) == 0:
            # check if input is infobox
            if "directors" in next(iter(f)):
                temp.append(f)

        elif len(temp) == 1:
            #check if input is title
            if "title" in next(iter(f)):
                # check if directors match
                if temp[0]['directors'] == f['directors']:
                    temp.append(f)
                    result.append(temp)
            temp = []
    return result

def create_node_info(list):

    #break down list
    for film in list:
        i,t = film

def write_to_csv(df,filepath):
    '''
    input: a pandas DataFrame

    writes to a csv file
    in same diretory as this script

    returns: nothing
    '''
    # if no csv exists
    if not path.exists(filepath):
        df.to_csv(filepath,index=False)
    else:
        df.to_csv(filepath, mode='a', header=False,index=False)

# load bacon and kaggle datasets
raw_bacon_data = load_txt_data(bacon_data_path)
kaggle_data = load_csv_data(corrected_kaggle_data_path)


# Drop any category not in categories_interest in kaggle dataset
kaggle_data = kaggle_data[kaggle_data['category'].isin(categories_interest)]

# clean list of info/title string dictionaies
clean_bacon_data = blob_to_list(raw_bacon_data)

# convert from list to pandas df
bacon_pair_list = create_info_title_pair_list(clean_bacon_data)
print(len(bacon_pair_list))
print(len(clean_bacon_data))
