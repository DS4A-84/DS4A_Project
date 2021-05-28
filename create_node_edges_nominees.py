#!/usr/bin/python

# DS4A Project
# Group 84
# Here we use the clean oracle of bacon dataset that only includes info
# on the nominees from the kaggle dataset



import pandas as pd




clean_bacon_df_path = 'data/clean_bacon_df.csv'



def load_dataset(filepath):
    df = pd.read_csv(filepath)
    return df



clean_bacon_df = load_dataset(clean_bacon_df_path)
'''
print(a.head())
                   title  year      role                name
0  The Birth of a Nation  1915      star        Lillian Gish
1  The Birth of a Nation  1915      cast        Donald Crisp
2           Blade Runner  1982      star       Harrison Ford
3           Blade Runner  1982      star  Edward James Olmos
4           Blade Runner  1982  director        Ridley Scott
'''

# to get edges
# for loop every title and create a new dataframe with columns source target
# do not include titles with only one nominee in it
edges = pd.DataFrame({'source':[], 'target':[]})
films = clean_bacon_df['title'].unique()

for i in films:
    a = clean_bacon_df[clean_bacon_df['title'] == i]
    print(a)
    exit()




# to get nodes
#per person condence film info into nested dictionary with each dictionary having
#the nominees film info
