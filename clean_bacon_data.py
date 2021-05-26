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


def write_clean_blob_to_txt(lines):
    '''
    Input: lines - readlines object
           filepath - str of output path

    Takes lines input and formats it to a python dictionary
    only keeps lines that are json blobs

    returns:  nested list of dictionaries, a  list is one movie
    '''

    dict = {
        "INFOBOX: ":"",
        "=>":":",
        "[[": "",
        "]]":"",
        "\n":""
        }

    temp = []
    result = []
    label = ""
    for i in lines:
        if 'INFOBOX' in i or '{"title' in i :
            temp_label = ""
            if 'INFOBOX' in i[0:10]:
                temp_label = "INFOBOX"
            else:
                temp_label = "title"

            #check for directors in
            if 'directors' not in i:
                temp = []
                continue

            # check if year of film exists
            if 'year' not in i:
                temp = []
                continue


            # clean the line
            i = reduce(lambda x, y: x.replace(y, dict[y]), dict, i)

            # check if label is the same as previous
            if label == temp_label:
                # if label is INFOBOX
                # then you throw away previous info and create new temp with
                # current info

                # if label is title skip


                temp = []
                temp.append(i)
                continue

            # check for title after info

            # convert to dictionary
            i = json.loads(i)
            temp.append(i)
            label = temp_label
            if len(temp) == 2:
                result.append(temp)
                temp = []

    if "title" in result[0]:
        print(result)
    return result

def convert_clean_blob_to_pandas_df(list):
    '''
    inputs - nested list of pairs of dictionaries

    takes in nested list dictionaies infobox and title
    converts both dictionaries per film to one pandas DataFrame

    returns: a large pandas dataframe of all the film dataframes
             vertically stacked
    '''

    df = pd.DataFrame({"title":[],"year":[],"role":[],"name":[]})

    temp = ""
    for film in list:
        i, t = film

        try:
            t['cast']
        except KeyError:
            print(temp)
            print(film)

        temp = film
        #if cast field is empty, skip
        if t['cast']:
            cast_df = pd.DataFrame({'title':[t['title']]*len(t['cast']),
                                    'year':[t['year']]*len(t['cast']),
                                    'role':["cast"]*len(t['cast']),
                                    'name':t['cast']
                                    })
            # fill in star info if any
            if 'stars' in i:
                for a in i['stars']:
                    cast_df.loc[cast_df['name'] == a,'role'] = "star"

            df.append(cast_df, ignore_index=True)

        #add director dataframe
        director_df = pd.DataFrame({'title':[t['title']]*len(t['directors']),
                                'year':[t['year']]*len(t['directors']),
                                'role':["director"]*len(t['directors']),
                                'name':t['directors']
                                })

        df.append(director_df, ignore_index=True)

    return df


# load bacon and kaggle datasets
raw_bacon_data = load_txt_data(bacon_data_path)
kaggle_data = load_csv_data(corrected_kaggle_data_path)

# Drop any category not in categories_interest in kaggle dataset
kaggle_data = kaggle_data[kaggle_data['category'].isin(categories_interest)]
clean_bacon_data = write_clean_blob_to_txt(raw_bacon_data)


# convert from list to pandas df
bacon_df = convert_clean_blob_to_pandas_df(clean_bacon_data)
