#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import opendatasets as od
import os

import warnings
warnings.filterwarnings("ignore")

# To pull bio data
def acquire_olympics_bio():
    """ Acquire Oplympic Biography Data"""
    
    if os.path.exists('Olympic_Athlete_Bio.csv'):
        bio = pd.read_csv('Olympic_Athlete_Bio.csv')
        return bio
    
    else:
        # Download File
        od.download("https://www.kaggle.com/datasets/josephcheng123456/olympic-historical-dataset-from-olympediaorg?select=Olympic_Athlete_Bio.csv")
        
        # Print to csv
        bio = pd.read_csv('./olympic-historical-dataset-from-olympediaorg/Olympic_Athlete_Bio.csv')
        bio.to_csv('Olympic_Athlete_Bio.csv', index=False)
              
        return bio

def acquire_olympics_er():
    """ Acquire Oplympic Event Results Data"""
    
    if os.path.exists('Olympic_Athlete_Event_Results.csv'):
        er = pd.read_csv('Olympic_Athlete_Event_Results.csv')
        return er
    
    else:
        # Download File
        od.download("https://www.kaggle.com/datasets/josephcheng123456/olympic-historical-dataset-from-olympediaorg?select=Olympic_Athlete_Bio.csv")
        event_res = './olympic-historical-dataset-from-olympediaorg/Olympic_Athlete_Event_Results.csv'
        er = pd.read_csv(event_res)
        er.to_csv('Olympic_Athlete_Event_Results.csv', index=False)
        return er

def acquire_olympics_mt():
    """ Acquire Oplympic Data"""
    
    if os.path.exists('Olympic_Games_Medal_Tally.csv'):
        mt = pd.read_csv('Olympic_Games_Medal_Tally.csv')
        return mt
    
    else:
        # Download File
        od.download("https://www.kaggle.com/datasets/josephcheng123456/olympic-historical-dataset-from-olympediaorg?select=Olympic_Athlete_Bio.csv")
        medal_tally ='./olympic-historical-dataset-from-olympediaorg/Olympic_Games_Medal_Tally.csv'
        mt = pd.read_csv(medal_tally)
        mt.to_csv('Olympic_Games_Medal_Tally.csv', index=False)
        return mt

def acquire_olympics_res():
    """ Acquire Oplympic results Data"""
    
    if os.path.exists('Olympic_Results.csv'):
        res = pd.read_csv('Olympic_Results.csv')
        return res
    
    else:
        # Download File
        od.download("https://www.kaggle.com/datasets/josephcheng123456/olympic-historical-dataset-from-olympediaorg?select=Olympic_Athlete_Bio.csv")
        results = './olympic-historical-dataset-from-olympediaorg/Olympic_Results.csv'
        res = pd.read_csv(results)
        res.to_csv('Olympic_Results.csv', index=False)
        return res
    
def acquire_olympics_country():
    """ Acquire Oplympic Country Data"""
    
    if os.path.exists('Olympics_Country.csv'):
        country = pd.read_csv('Olympics_Country.csv')
        return country
    
    else:
        # Download File
        od.download("https://www.kaggle.com/datasets/josephcheng123456/olympic-historical-dataset-from-olympediaorg?select=Olympic_Athlete_Bio.csv")
        country ='./olympic-historical-dataset-from-olympediaorg/Olympics_Country.csv'
        country = pd.read_csv(country)
        country.to_csv('Olympics_country.csv', index= False)
        return country

def acquire_olympics_games():
    """ Acquire Oplympic Game Data"""
    
    if os.path.exists('Olympics_Games.csv'):
        games = pd.read_csv('Olympics_Games.csv')
        return games
    
    else:
        # Download File
        od.download("https://www.kaggle.com/datasets/josephcheng123456/olympic-historical-dataset-from-olympediaorg?select=Olympic_Athlete_Bio.csv")
        games = './olympic-historical-dataset-from-olympediaorg/Olympics_Games.csv'
        games = pd.read_csv(games)
        games.to_csv('Olympics_Games.csv', index=False)
        return games

def pull_data():
    acquire_olympics_bio()
    acquire_olympics_er()
    acquire_olympics_mt()
    acquire_olympics_res()
    acquire_olympics_country()
    acquire_olympics_games()
    print('Olympic data pulled')

    #. To copy and paste in jupyter notebook
# bio = pd.read_csv('Olympic_Athlete_Bio.csv')
# er = pd.read_csv('Olympic_Athlete_Event_Results.csv')
# res = pd.read_csv('Olympic_Results.csv')
# country = pd.read_csv('Olympics_country.csv')
# games = pd.read_csv('Olympics_Games.csv')
# mt = pd.read_csv('Olympic_Games_Medal_Tally.csv')

def merge_data(bio, er, res, country, games):
    # merge bio and event results
    olympics=pd.merge(bio, er[['edition','sport', 'event', 'result_id','medal', 'isTeamSport', 'athlete_id']], on ='athlete_id', how='left')
    # Merge olypics and results infromation
    olympics=pd.merge(olympics,res[['result_participants','result_id']], on='result_id', how='left')
    # mergeolympics and games information
    olympics=pd.merge(olympics,games[['year', 'city','edition','country_noc']], on='edition', how='left')
    #Join country code of Host country
    #olympics=pd.merge(olympics,country, on=['country_noc_y','country_noc'], how='left')
    #olympics.join(games.set_index(['country_noc','country']). on=['country_noc', 'country_noc_y'], how='left')
    print("Use df: 'olympics'")
    return olympics
