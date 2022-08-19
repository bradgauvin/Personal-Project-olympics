#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import opendatasets as od
import os
import re
from datetime import datetime

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
# bio = pd.read_csv('clean_olympic_athlete_bio.csv')
# er = pd.read_csv('Olympic_Athlete_Event_Results.csv')
# res = pd.read_csv('Olympic_Results.csv')
# country = pd.read_csv('Olympics_country.csv')
# games = pd.read_csv('Olympics_Games.csv')
# mt = pd.read_csv('Olympic_Games_Medal_Tally.csv')

# - Replace null values in all columns to 'na'
# - Convert all string date values to date objects (dd MONTH_String yyyy or just yyyy) to yyyy-mm-dd

def athlete_bio():
    bio = pd.read_csv('./olympic-historical-dataset-from-olympediaorg/Olympic_Athlete_Bio.csv')
    bio.fillna('na', inplace=True)

    for index, row in bio.iterrows():
        born = row['born']
        pattern_year_only = re.compile('^\d\d\d\d$')
        pattern_day_month_year = re.compile('^[\d]* [a-zA-z]* [\d]*')
        pattern_month_year = re.compile('^[a-zA-z]* \d\d\d\d')

        if born == 'na':
            continue
        elif pattern_year_only.match(born): # when there's only the year they are born in - assume they are born in January 1st of the year
            date_object = datetime.strptime(born, '%Y').date()
            bio.loc[index, 'born'] = date_object
        elif pattern_day_month_year.match(born):
            date_object = datetime.strptime(born, '%d %B %Y').date()
            bio_df.loc[index, 'born'] = date_object
        elif pattern_month_year.match(born):
            date_object = datetime.strptime(born, '%B %Y').date()
        else:
            continue

        bio.loc[index, 'born'] = date_object
    # Save Dataframe to CSV file
    bio.to_csv('./clean_olympic_athlete_bio.csv', index=False)
    # bio.to_csv('./Personal-Project-olympics/bio.csv', index=False)

def merge_data(bio, er, res, country, games):
    # merge bio and event results
    olympics=pd.merge(bio, er[['edition','sport', 'event', 'result_id','medal', 'isTeamSport', 'athlete_id']], on ='athlete_id', how='left')
    # Merge olypics and results infromation - Not using As medals are focus area
    #olympics=pd.merge(olympics,res[['result_participants','result_id']], on='result_id', how='left')
    # mergeolympics and games information
    olympics=pd.merge(olympics,games[['year', 'city','edition','country_noc']], on='edition', how='left')
    #Join country code of Host country
    #olympics=pd.merge(olympics,country, on=['country_noc_y','country_noc'], how='left')
    #olympics.join(games.set_index(['country_noc','country']). on=['country_noc', 'country_noc_y'], how='left')
    print("Use df: 'olympics'")
    return olympics

def wrangle_olympics(df):
    
    # # Changes and updates:
    # Delete unecessary Columns
    olympics = df.drop(['description','special_notes'], axis=1)
    # Change Born to date format - what to do with NA values
    olympics['born'].str.strip()
    olympics['born'] = pd.to_datetime(olympics['born'], errors='ignore', format="%Y-%m-%d")
    # Building event_year because 'year' has missing values
    olympics['event_year'] = olympics['edition'].str[:4]
    # Cleared 'year' due to missing values
    olympics = olympics.drop(columns='year')
    # Height Change to int.
    # Edition - Take off year
    olympics['edition'] = olympics['edition'].str[4:]
    # Medal - Change na to participant
    olympics.medal.replace('na','participant',inplace=True)
    # Create Medalist column
    olympics['medalist']= np.where(olympics['medal'] != 'participant', 1, 0)
    # Create Column Home - for athletes competing in host contry
    olympics['home']=olympics.country_noc_x == olympics.country_noc_y
    # Convert Bool to int
    olympics['isTeamSport']=olympics.isTeamSport.astype('int')
    olympics['home']=olympics.home.astype('int')
    # Delete Equestrian olymics of 1956 and Interrelated games of 1906
    olympics = olympics[olympics['city'].notna()]
    # Replace 'na' values with nulls
    olympics = olympics.replace('na', None)

    return olympics

def replace_olympics(df):
    """ Dataset has multiple items in date born, replacing any dates as Jan 01 of year mentioned
    On weight, multiple measures and weight classes were used.  This adjusts to lowest weight mentioned"""
    olympics = df.replace('na', None)
    olympics = olympics.replace('in Herstal (BEL)', None)
    olympics = olympics.replace('(circa 1925)', '1925-01-01')
    olympics = olympics.replace('(circa 1924)', '1924-01-01')
    olympics = olympics.replace('in Al-Qahira (Cairo) (EGY)', None)
    olympics = olympics.replace('in Al-Iskanderiya (Alexandria) (EGY)', None)
    olympics = olympics.replace('in Verona, Verona (ITA)', None)
    olympics = olympics.replace('(circa 1921)', '1921-01-01')
    olympics = olympics.replace('in ?, Hiroshima (JPN)', None)
    olympics = olympics.replace('in Tanta (EGY) (c. 1924)', '1924-01-01')
    olympics = olympics.replace('(1946 or 1947)', '1946-01-01')
    olympics = olympics.replace('(circa 1926)', '1926-01-01')
    olympics = olympics.replace('(1941 or 1942)', '1941-01-01')
    olympics = olympics.replace('in Karaj (IRI)',None)
    olympics = olympics.replace('(circa 1936)', '1936-01-01')
    olympics = olympics.replace('in Kuala Lumpur (MAS) (circa 1920)','1920-01-01')
    olympics = olympics.replace('166-187', '166')
    olympics = olympics.replace('(1942 or 1943)', '1942-01-01')
    olympics = olympics.replace('in Uchila, Udupi, Karnataka (IND)',None)
    olympics = olympics.replace('in Jičín (CZE)',None)
    olympics = olympics.replace ('(circa 1928)','1928-01-01')
    olympics = olympics.replace('in Barcelona, Barcelona (ESP)', None)
    olympics = olympics.replace('in Spetses (GRE)',None)
    olympics = olympics.replace('in Ipoh (MAS) (circa 1927)','1927-01-01')
    olympics = olympics.replace('in Geili (SUD)',None)
    olympics = olympics.replace('in Santiago (CHI)', None)
    olympics = olympics.replace('(1952 or 1953)','1952-01-01')
    olympics = olympics.replace('in ? (MAS)', None)
    olympics = olympics.replace('in Cento, Ferrara (ITA)', None)
    olympics = olympics.replace('in ?, England (GBR)', None)
    olympics = olympics.replace('(circa 1920)', '1920-01-01')
    olympics = olympics.replace('in Scotland (GBR)', None)
    olympics = olympics.replace('(1926 or 1927)', '1926-01-01')
    olympics = olympics.replace('(circa 1932)', '1932-01-01')
    olympics = olympics.replace('in Napoli, Napoli (ITA)', None)
    olympics = olympics.replace('(born 1904/1905)', '1904-01-01')
    olympics = olympics.replace('in Ipoh (MAS)', None)
    olympics = olympics.replace('(circa 1911)', '1911-01-01')
    olympics = olympics.replace('(circa 1915)', '1915-01-01')
    olympics = olympics.replace('(circa 1934)', '1934-01-01')
    olympics = olympics.replace('(circa 1909)', '1909-01-01')
    olympics = olympics.replace('in Puerto Barrios (GUA)', None)
    olympics = olympics.replace('(circa 1927)', '1927-01-01')
    olympics = olympics.replace('in Dublin (IRL)', None)
    olympics = olympics.replace('(1916 or 1917)', '1916-01-01')
    olympics = olympics.replace('in ?, Kriti (GRE)', None)
    olympics = olympics.replace('(circa 1933)', '1933-01-01')
    olympics = olympics.replace('in La Carlota (ARG)', None)
    olympics = olympics.replace('in Cheolweon (KOR)', None)
    olympics = olympics.replace('in Santiago (CHI) (circa 1925)', "1925-01-01")
    olympics = olympics.replace('in Antwerpen (Antwerp) (BEL)', None)
    olympics = olympics.replace('in Seremban (MAS)', None)
    olympics = olympics.replace('(1945 or 1946)', '1945-01-01')
    olympics = olympics.replace('(1920 or 1921)', '1920-01-01')
    olympics = olympics.replace('in Senahú (GUA)', None)
    olympics = olympics.replace('in Athina (Athens) (GRE)', None)
    olympics = olympics.replace('in Athina (Athens) (GRE)', None)
    olympics = olympics.replace('(circa 1929)', '1929-01-01')
    olympics = olympics.replace('(1901 or 1902)', '1901-01-01')
    olympics = olympics.replace('in ? (SUD)', None)
    olympics = olympics.replace('in Zittau, Sachsen (GER)', None)
    olympics = olympics.replace('in Miguel Hidalgo, Ciudad de México (MEX) (c. 1934)', "1934-01-01")
    olympics = olympics.replace('in Rio de Janeiro, Rio de Janeiro (BRA)', None)
    olympics = olympics.replace('(circa 1917)', '1917-01-01')
    olympics = olympics.replace('(1949 or 1950)', '1949-01-01')
    olympics = olympics.replace('in Kuala Lumpur (MAS) (circa 1921)', '1921-01-01')
    olympics = olympics.replace('in Guayaquil (ECU)', None)
    olympics = olympics.replace('in Ferrara, Ferrara (ITA)', None)
    olympics = olympics.replace('in Sinaia (ROU)', None)
    olympics = olympics.replace('in Wambaix, Nord (FRA)', None)
    olympics = olympics.replace('in Taiping (MAS)', None)
    olympics = olympics.replace('(1923 or 1924)', '1923-01-01')
    olympics = olympics.replace('in Randers (DEN)', None)
    olympics = olympics.replace('(1922 or 1923)', '1922-01-01')
    olympics = olympics.replace('in Cluny, Saône-et-Loire (FRA)', None)
    olympics = olympics.replace('(circa 1935)', '1935-01-01')
    olympics = olympics.replace('(1963 or 1964)', '1963-01-01')
    olympics = olympics.replace('(1948 or 1949)', '1948-01-01')
    olympics = olympics.replace('(1917 or 1918)', '1917-01-01')
    olympics = olympics.replace('(circa 1919)', '1919-01-01')
    olympics = olympics.replace('(1915 or 1916)', '1915-01-01')
    olympics = olympics.replace('(1888 or 1889)', '1888-01-01')
    olympics = olympics.replace('in Kathmandu (NEP)', None)
    olympics = olympics.replace('(1921 or 1922)', '1921-01-01')
    olympics = olympics.replace('(1947 or 1948)', '1947-01-01')
    olympics = olympics.replace('in Lima (PER)', None)
    olympics = olympics.replace('in Tiruvalla, Kerala (IND)', None)
    olympics = olympics.replace('(circa 1902)', '1902-01-01')
    olympics = olympics.replace('in Milano, Milano (ITA)', None)
    olympics = olympics.replace('in Valtournenche, Aosta (ITA)', None)
    olympics = olympics.replace('in Schiedam (NED)', None)
    olympics = olympics.replace('(circa 1923)', '1923-01-01')
    olympics = olympics.replace('in Arad (ROU)', None)
    olympics = olympics.replace('(circa 1912)', '1912-01-01')
    olympics = olympics.replace('(1932 or 1933)', '1932-01-01')
    olympics = olympics.replace('in Des Moines, Iowa (USA)', None)
    olympics = olympics.replace('in Kuala Lumpur (MAS) (circa 1929)', "1929-01-01")
    olympics = olympics.replace('in Hyderabad (PAK)', None)
    olympics = olympics.replace('in Bogotá (COL)', None)
    olympics = olympics.replace('in Akharnes (GRE)', None)
    olympics = olympics.replace('in Villabona, Guipúzcoa (ESP)', None)
    olympics = olympics.replace('in Palmerston (NZL)', None)
    olympics = olympics.replace('in Innsbruck (AUT)', None)
    olympics = olympics.replace('in Rabenstein, Zwiesel, Bayern (GER)', None)
    olympics = olympics.replace('(1919 or 1920)', '1919-01-01')
    olympics = olympics.replace('in Firenze, Firenze (ITA)', None)
    olympics = olympics.replace('in Asyut (EGY)', None)
    olympics = olympics.replace('in München (Munich), Bayern (GER)', None)
    olympics = olympics.replace('in Pyeongyang (PRK)', None)
    olympics = olympics.replace('in Paris, Paris (FRA)', None)
    olympics = olympics.replace('(circa 1914)', '1914-01-01')
    olympics = olympics.replace('(1951 or 1952)', '1951-01-01')
    olympics = olympics.replace('(circa 1931)', '1931-01-01')
    olympics = olympics.replace('in Jalpaiguri, West Bengal (IND)', None)
    olympics = olympics.replace('in Beirut (LBN)', None)
    olympics = olympics.replace('in Tolosa, Guipúzcoa (ESP)', None)
    olympics = olympics.replace('in Yerres, Essonne (FRA)', None)
    olympics = olympics.replace('in Oran (ALG)', None)
    olympics = olympics.replace('in Evrytania (GRE)', None)
    olympics = olympics.replace('(1924 or 1925)', '1924-01-01')
    olympics = olympics.replace('in Nepalgunj (NEP) (1961 or 1962)', '1961-01-01')
    olympics = olympics.replace('(circa 1922)', '1922-01-01')
    olympics = olympics.replace('in Trieste, Trieste (ITA)', None)
    olympics = olympics.replace('in Montevideo (URU)', None)
    olympics = olympics.replace('in Berehove, Zakarpattia (UKR)', None)
    olympics = olympics.replace('in Bur Said (Port Said) (EGY)', None)
    olympics = olympics.replace('in ?, Chaharmahal-o-Bakhtiyari (IRI)', None)
    olympics = olympics.replace('in Kalavryta (GRE)', None)
    olympics = olympics.replace('in Gent (Ghent) (BEL)', None)
    olympics = olympics.replace('in Brescia, Brescia (ITA)', None)
    olympics = olympics.replace('(1896 or 1897)', '1896-01-01')
    olympics = olympics.replace('in Genève (Geneva) (SUI)', None)
    olympics = olympics.replace('in Glasgow, Glasgow City, Scotland (GBR)', None)
    olympics = olympics.replace('(1912 or 1913)', '1912-01-01')
    olympics = olympics.replace('(1880 or 1881)', '1880-01-01')
    olympics = olympics.replace('77-80', '77')
    olympics = olympics.replace('85-92', '85')
    olympics = olympics.replace('68-72', '68')
    olympics = olympics.replace('90-105','90')
    olympics = olympics.replace('90-93', '90')
    olympics = olympics.replace('51-53','51')
    olympics = olympics.replace('69-70','69')
    olympics = olympics.replace('72-74', '72')
    olympics = olympics.replace('75-79', '75')
    olympics = olympics.replace('57-64','57')
    olympics = olympics.replace('88-96','88')
    olympics = olympics.replace('84-86', '84')
    olympics = olympics.replace('132-135', '132')
    olympics = olympics.replace('132-135', '132')
    olympics = olympics.replace('60-62', '60')
    olympics = olympics.replace('75-78', '75')
    olympics = olympics.replace('64-66', '64')
    olympics = olympics.replace('52-55', '52')
    olympics = olympics.replace('80, 86', '80')
    olympics = olympics.replace('66-68', '66')
    olympics = olympics.replace('52-56', '52')
    olympics = olympics.replace('59-67', '59')
    olympics = olympics.replace('59-60', '59')
    olympics = olympics.replace('100-113', '100')
    olympics = olympics.replace('90-95', '90')
    olympics = olympics.replace('68-70', '68')
    olympics = olympics.replace('73-76', '73')
    olympics = olympics.replace('64-65', '64')
    olympics = olympics.replace('97-105', '97')
    olympics = olympics.replace('91-93', '91')
    olympics = olympics.replace('78-80', '78')
    olympics = olympics.replace('58-73', '58')
    olympics = olympics.replace('66-76', '66')
    olympics = olympics.replace('52-53', '52')
    olympics = olympics.replace('165-175', '165')
    olympics = olympics.replace('67-72', '67')
    olympics = olympics.replace('85-90', '85')
    olympics = olympics.replace('75-80', '165')
    olympics = olympics.replace('48-52', '48')
    olympics = olympics.replace('67-74', '67')
    olympics = olympics.replace('74-78', '74')
    olympics = olympics.replace('63-64', '63')
    olympics = olympics.replace('82-87', '82')
    olympics = olympics.replace('118-138', '118')
    olympics = olympics.replace('67-69', '67')
    olympics = olympics.replace('77-79', '77')
    olympics = olympics.replace('51-52', '51')
    olympics = olympics.replace('82-85', '82')
    olympics = olympics.replace('84-88', '84')
    olympics = olympics.replace('51-57', '51')
    olympics = olympics.replace('65-72', '65')
    olympics = olympics.replace('82-86', '82')
    olympics = olympics.replace('63-68', '63')
    olympics = olympics.replace('83-90', '83')
    olympics = olympics.replace('94-103', '94')
    olympics = olympics.replace('70-73', '70')
    olympics = olympics.replace('70-72', '70')
    olympics = olympics.replace('72-80', '72')
    olympics = olympics.replace('63-65', '63')
    olympics = olympics.replace('72-75', '72')
    olympics = olympics.replace('90-94', '90')
    olympics = olympics.replace('110-115', '110')
    olympics = olympics.replace('80-86', '80')
    olympics = olympics.replace('62-69', '62')
    olympics = olympics.replace('62-66', '62')
    olympics = olympics.replace('66-73', '66')
    olympics = olympics.replace('55-58', '55')
    olympics = olympics.replace('75-77', '75')
    olympics = olympics.replace('62-67', '62')
    olympics = olympics.replace('80-82', '80')
    olympics = olympics.replace('89-92', '89')
    olympics = olympics.replace('78-85', '78')
    olympics = olympics.replace('73-75', '73')
    olympics = olympics.replace('106-110', '106')
    olympics = olympics.replace('124, 131', '124')
    olympics = olympics.replace('109-141', '109')
    olympics = olympics.replace('55-59', '55')
    olympics = olympics.replace('149-163', '149')
    olympics = olympics.replace('63-67', '63')
    olympics = olympics.replace('130-141', '130')
    olympics = olympics.replace('77-81', '77')
    olympics = olympics.replace('49-50', '49')
    olympics = olympics.replace('75-81', '75')
    olympics = olympics.replace('76-80', '76')
    olympics = olympics.replace('83-95', '83')
    olympics = olympics.replace('58-62', '58')
    olympics = olympics.replace('92-96', '92')
    olympics = olympics.replace('78-82', '78')
    olympics = olympics.replace('70-84', '70')
    olympics = olympics.replace('79-80', '79')
    olympics = olympics.replace('82-100', '82')
    olympics = olympics.replace('87-90', '87')
    olympics = olympics.replace('75-76', '75')
    olympics = olympics.replace('52-58', '52')
    olympics = olympics.replace('81-84', '81')
    olympics = olympics.replace('89-97', '89')
    olympics = olympics.replace('59-65', '59')
    olympics = olympics.replace('63-70', '63')
    olympics = olympics.replace('74, 75', '74')
    olympics = olympics.replace('98-102', '98')
    olympics = olympics.replace('64-68', '64')
    olympics = olympics.replace('140-152', '140')
    olympics = olympics.replace('78-103', '78')
    olympics = olympics.replace('60-63', '60')
    olympics = olympics.replace('97-103', '97')
    olympics = olympics.replace('79-82', '79')
    olympics = olympics.replace('66-67', '66')
    olympics = olympics.replace('81-98', '81')
    olympics = olympics.replace('88-91', '88')
    olympics = olympics.replace('74-75', '74')
    olympics = olympics.replace('87-89', '87')
    olympics = olympics.replace('105-111', '105')
    olympics = olympics.replace('106-112', '106')
    olympics = olympics.replace('58, 68', '58')
    olympics = olympics.replace('110-118', '110')
    olympics = olympics.replace('65-68', '65')
    olympics = olympics.replace('52-62', '52')
    olympics = olympics.replace('95-105', '95')
    olympics = olympics.replace('76-82', '76')
    olympics = olympics.replace('108-112', '108')
    olympics = olympics.replace('56-58', '56')
    olympics = olympics.replace('57-63', '57')
    olympics = olympics.replace('48-82', '48')
    olympics = olympics.replace('58-68', '58')
    olympics = olympics.replace('105-114', '105')
    olympics = olympics.replace('62-68', '62')
    olympics = olympics.replace('71-73', '71')
    olympics = olympics.replace('90-108', '90')
    olympics = olympics.replace('80-85', '80')
    olympics = olympics.replace('75-82', '75')
    olympics = olympics.replace('90-110', '90')
    olympics = olympics.replace('60-64', '60')
    olympics = olympics.replace('64-73', '64')
    olympics = olympics.replace('56-65', '56')
    olympics = olympics.replace('60-70', '60')
    olympics = olympics.replace('95-99', '99')
    olympics = olympics.replace('83-88', '83')
    olympics = olympics.replace('53-55', '55')
    olympics = olympics.replace('80-84', '80')
    olympics = olympics.replace('48-50', '48')
    olympics = olympics.replace('58-60', '58')
    olympics = olympics.replace('54-56', '54')
    olympics = olympics.replace('86-88', '86')
    olympics = olympics.replace('87-93', '87')
    olympics = olympics.replace('74-76', '74')
    olympics = olympics.replace('76-78', '76')
    olympics = olympics.replace('82-90', '82')
    olympics = olympics.replace('67-68', '67')
    olympics = olympics.replace('74-82', '74')
    olympics = olympics.replace('65-71', '65')
    olympics = olympics.replace('52-72', '52')
    olympics = olympics.replace('79-83', '79')
    olympics = olympics.replace('52-54', '52')
    olympics = olympics.replace('77,5', '77')
    olympics = olympics.replace('65-74', '65')
    olympics = olympics.replace('54-58', '54')
    olympics = olympics.replace('56-60', '56')
    olympics = olympics.replace('85-89', '85')
    olympics = olympics.replace('90-92', '90')
    olympics = olympics.replace('54-57', '54')
    olympics = olympics.replace('108-140', '108')
    olympics = olympics.replace('158-168', '158')
    olympics = olympics.replace('62, 67', '62')
    olympics = olympics.replace('81-90', '81')
    olympics = olympics.replace('83-87', '83')
    olympics = olympics.replace('62-65', '62')
    olympics = olympics.replace('55-56', '55')
    olympics = olympics.replace('210-218', '210')
    olympics = olympics.replace('66-70', '60')
    olympics = olympics.replace('95-98', '95')
    olympics = olympics.replace('48-54', '48')
    olympics = olympics.replace('62-64', '62')
    olympics = olympics.replace('97-104', '97')
    olympics = olympics.replace('68-76', '68')
    olympics = olympics.replace('125-129', '125')
    olympics = olympics.replace('60-68', '60')
    olympics = olympics.replace('90-102', '90')
    olympics = olympics.replace('57-58', '57')
    olympics = olympics.replace('77-85', '77')
    olympics = olympics.replace('56-62', '56')
    olympics = olympics.replace('70-76', '70')
    olympics = olympics.replace('104-128', '104')
    olympics = olympics.replace('50-52', '50')
    olympics = olympics.replace('70-75', '70')
    olympics = olympics.replace('84-92', '84')
    olympics = olympics.replace('65-70', '65')
    olympics = olympics.replace('67-75', '67')
    olympics = olympics.replace('100-104', '100')
    olympics = olympics.replace('82-84', '82')
    olympics = olympics.replace('81-83', '81')
    olympics = olympics.replace('52-57', '52')
    olympics = olympics.replace('62-63', '62')
    olympics = olympics.replace('60-65', '60')
    olympics = olympics.replace('89-103', '89')
    olympics = olympics.replace('71-74', '71')
    olympics = olympics.replace('79-81', '79')
    olympics = olympics.replace('71-77', '71')
    olympics = olympics.replace('74-77', '74')
    olympics = olympics.replace('67-70', '67')
    olympics = olympics.replace('81-82', '81')
    olympics = olympics.replace('75-91', '75')
    olympics = olympics.replace('68, 88', '68')
    olympics = olympics.replace('83-86', '83')
    olympics = olympics.replace('65-67', '65')
    olympics = olympics.replace('58-63', '58')
    olympics = olympics.replace('89-96', '89')
    olympics = olympics.replace('70-83', '70')
    olympics = olympics.replace('63-71', '63')
    olympics = olympics.replace('70-74', '70')
    olympics = olympics.replace('53-58', '53')
    olympics = olympics.replace('57-62', '57')
    olympics = olympics.replace('135-140', '135')
    olympics = olympics.replace('72-76', '72')
    olympics = olympics.replace('60-67', '60')
    olympics = olympics.replace('98-103', '98')
    olympics = olympics.replace('106-111', '106')
    olympics = olympics.replace('100-105', '100')
    olympics = olympics.replace('53-56', '53')
    olympics = olympics.replace('85-94', '85')
    olympics = olympics.replace('75-84', '75')
    olympics = olympics.replace('70-87', '70')
    olympics = olympics.replace('82-92', '82')
    olympics = olympics.replace('59-62', '59')
    olympics = olympics.replace('88-94', '88')
    olympics = olympics.replace('142-158', '142')
    olympics = olympics.replace('69-75', '69')
    olympics = olympics.replace('117-121', '117')
    olympics = olympics.replace('78-90', '78')
    olympics = olympics.replace('73-74', '73')
    olympics = olympics.replace('119-125', '119')
    olympics = olympics.replace('82-102', '82')
    olympics = olympics.replace('62-74', '62')
    olympics = olympics.replace('91-95', '91')
    olympics = olympics.replace('88-90', '88')
    olympics = olympics.replace('108-152', '108')
    olympics = olympics.replace('89, 107', '89')
    olympics = olympics.replace('130-132', '130')
    olympics = olympics.replace('76-81', '76')
    olympics = olympics.replace('88-89', '88')
    olympics = olympics.replace('54-55', '54')
    olympics = olympics.replace('65-66', '65')
    olympics = olympics.replace('105-110', '105')
    olympics = olympics.replace('68-71', '68')
    olympics = olympics.replace('87-92', '87')
    olympics = olympics.replace('78-79', '78')
    olympics = olympics.replace('79-88', '79')
    olympics = olympics.replace('70-77', '70')
    olympics = olympics.replace('78-88', '78')
    olympics = olympics.replace('100, 104', '100')
    olympics = olympics.replace('93-100', '93')
    olympics = olympics.replace('80-83', '80')
    olympics = olympics.replace('55-60', '55')
    olympics = olympics.replace('61-65', '61')
    olympics = olympics.replace('59-61', '59')
    olympics = olympics.replace('69-71', '69')
    olympics = olympics.replace('95-100', '95')
    olympics = olympics.replace('82-88', '82')
    olympics = olympics.replace('77-78', '77')
    olympics = olympics.replace('127-129', '127')
    olympics = olympics.replace('75-85', '75')
    olympics = olympics.replace('83-91', '83')
    olympics = olympics.replace('92-94', '92')
    olympics = olympics.replace('76-77', '76')
    olympics = olympics.replace('91-96', '91')
    olympics = olympics.replace('155-160', '155')
    olympics = olympics.replace('81-85', '81')
    olympics = olympics.replace('81-87', '81')
    olympics = olympics.replace('88-92', '88')
    olympics = olympics.replace('68-74', '68')
    olympics = olympics.replace('147-163', '147')
    olympics = olympics.replace('98-105', '98')
    olympics = olympics.replace('51-58', '51')
    olympics = olympics.replace('57-61', '57')
    olympics = olympics.replace('110-123', '110')
    olympics = olympics.replace('60-66', '60')
    olympics = olympics.replace('80-140', '80')
    olympics = olympics.replace('88-95', '88')
    olympics = olympics.replace('82-89', '82')
    olympics = olympics.replace('102, 105', '102')
    olympics = olympics.replace('121-126', '121')
    olympics = olympics.replace('60-61', '60')
    olympics = olympics.replace('70-78', '70')
    olympics = olympics.replace('87-91', '87')
    olympics = olympics.replace('95-97', '95')
    olympics = olympics.replace('130-133', '130')
    olympics = olympics.replace('48-57', '48')
    olympics = olympics.replace('67, 71', '67')
    olympics = olympics.replace('75-92', '75')
    olympics = olympics.replace('64-69', '64')
    olympics = olympics.replace('86-90', '86')
    olympics = olympics.replace('126-133', '126')
    olympics = olympics.replace('85-88', '85')
    olympics = olympics.replace('90-121', '90')
    olympics = olympics.replace('52-82', '52')
    olympics = olympics.replace('62-73', '62')
    olympics = olympics.replace('50-62', '50')
    olympics = olympics.replace('73-80', '73')
    olympics = olympics.replace('49-53', '49')
    olympics = olympics.replace('87-100', '87')
    olympics = olympics.replace('115-130', '115')
    olympics = olympics.replace('48-63', '48')
    olympics = olympics.replace('80-90', '80')
    olympics = olympics.replace('80-92', '80')
    olympics = olympics.replace('48-58', '48')
    olympics = olympics.replace('80-81', '80')
    olympics = olympics.replace('68-69', '68')
    olympics = olympics.replace('104-107', '104')
    olympics = olympics.replace('80-87', '80')
    olympics = olympics.replace('117-125', '117')
    olympics = olympics.replace('51-61', '51')
    olympics = olympics.replace('46-50', '46')
    olympics = olympics.replace('61-62', '61')
    olympics = olympics.replace('52-60', '52')
    olympics = olympics.replace('57-59', '57')
    olympics = olympics.replace('72-79', '72')
    olympics = olympics.replace('86-94', '86')
    olympics = olympics.replace('78-81', '78')
    olympics = olympics.replace('70-80', '70')
    olympics = olympics.replace('69-80', '69')
    olympics = olympics.replace('110-116', '110')
    olympics = olympics.replace('84-85', '84')
    olympics = olympics.replace('48-49', '48')
    olympics = olympics.replace('94-86', '94')
    olympics = olympics.replace('90-100', '90')
    olympics = olympics.replace('116-132', '116')
    olympics = olympics.replace('53-57', '53')
    olympics = olympics.replace('100-106', '100')
    olympics = olympics.replace('70-71', '70')
    olympics = olympics.replace('56-57', '56')
    olympics = olympics.replace('102-106', '102')
    olympics = olympics.replace('86-92', '86')
    olympics = olympics.replace('57-68', '57')
    olympics = olympics.replace('84-56', '84')
    olympics = olympics.replace('54-60', '54')
    olympics = olympics.replace('73-77', '73')
    olympics = olympics.replace('70-82', '70')
    olympics = olympics.replace('74-90', '74')
    olympics = olympics.replace('48-65', '48')
    olympics = olympics.replace('71-75', '71')
    olympics = olympics.replace('67, 69', '67')
    olympics = olympics.replace('64-75', '64')
    olympics = olympics.replace('57-67', '57')
    olympics = olympics.replace('140-142', '140')
    olympics = olympics.replace('69-77', '69')
    olympics = olympics.replace('68-73', '68')
    olympics = olympics.replace('84-96', '84')
    olympics = olympics.replace('59-64', '59')
    olympics = olympics.replace('157-165', '157')
    olympics = olympics.replace('120-140', '120')
    olympics = olympics.replace('54-64', '54')
    olympics = olympics.replace('77-82', '77')
    olympics = olympics.replace('66-74', '66')
    olympics = olympics.replace('74-86', '74')
    olympics = olympics.replace('105-132', '105')
    olympics = olympics.replace('99-101', '99')
    olympics = olympics.replace('79-86', '79')
    olympics = olympics.replace('105-113', '105')
    olympics = olympics.replace('61-67', '61')
    olympics = olympics.replace('125-136', '125')
    olympics = olympics.replace('100-110', '100')
    olympics = olympics.replace('63, 66', '63')
    olympics = olympics.replace('74-80', '74')
    olympics = olympics.replace('92-95', '92')
    olympics = olympics.replace('74-83', '74')
    olympics = olympics.replace('93-104', '93')
    olympics = olympics.replace('95-113', '95')
    olympics = olympics.replace('95-102', '95')
    olympics = olympics.replace('52-59', '52')
    olympics = olympics.replace('120-125', '120')
    olympics = olympics.replace('104-105', '104')
    olympics = olympics.replace('73-79', '73')
    olympics = olympics.replace('58-64', '58')
    olympics = olympics.replace('106-108', '106')
    olympics = olympics.replace('55-57', '55')
    olympics = olympics.replace('76-94', '76')
    olympics = olympics.replace('68-75', '68')
    olympics = olympics.replace('67-81', '67')
    olympics = olympics.replace('91-94', '91')
    olympics = olympics.replace('64-67', '64')
    olympics = olympics.replace('85-87', '85')
    olympics = olympics.replace('142-151', '142')
    olympics = olympics.replace('132-145', '132')
    olympics = olympics.replace('132-145', '132')
    olympics = olympics.replace('82-120', '82')
    olympics = olympics.replace('83-93', '83')
    olympics = olympics.replace('68-88', '68')
    olympics = olympics.replace('75-83', '75')
    olympics = olympics.replace('69-76', '69')
    olympics = olympics.replace('159-163', '159')
    olympics = olympics.replace('66, 67', '66')
    olympics = olympics.replace('63-66', '63')
    olympics = olympics.replace('60-75', '60')
    olympics = olympics.replace('56-66', '56')
    olympics = olympics.replace('101-125', '101')
    olympics = olympics.replace('75-89', '75')
    olympics = olympics.replace('95-103', '95')
    olympics = olympics.replace('115-120', '115')
    olympics = olympics.replace('92-97', '92')
    olympics = olympics.replace('105-109', '105')
    olympics = olympics.replace('67-76', '67')
    olympics = olympics.replace('82-93', '82')
    olympics = olympics.replace('90-96', '90')
    olympics = olympics.replace('107-136', '107')
    olympics = olympics.replace('78, 80', '78')
    olympics = olympics.replace('95-110', '95')
    olympics = olympics.replace('76, 83', '76')
    olympics = olympics.replace('81-89', '81')
    olympics = olympics.replace('86, 90', '86')
    olympics = olympics.replace('130-140', '130')
    olympics = olympics.replace('107-118', '107')
    olympics = olympics.replace('109-125', '109')
    olympics = olympics.replace('62-70', '62')
    olympics = olympics.replace('53-54', '53')
    olympics = olympics.replace('116-130', '116')
    olympics = olympics.replace('67, 72', '67')
    olympics = olympics.replace('125-127', '125')
    olympics = olympics.replace('68, 80', '68')
    olympics = olympics.replace('74-81', '74')
    olympics = olympics.replace('83-104', '83')
    olympics = olympics.replace('68-87', '68')
    olympics = olympics.replace('74, 81', '74')
    olympics = olympics.replace('86-89', '86')
    olympics = olympics.replace('81-86', '81')
    olympics = olympics.replace('85-86', '85')
    olympics = olympics.replace('82-98', '82')
    olympics = olympics.replace('90-97', '90')
    olympics = olympics.replace('55-62', '55')
    olympics = olympics.replace('62-100', '62')
    olympics = olympics.replace('95-115', '95')
    olympics = olympics.replace('89, 115', '89')
    
    return olympics

def height_weight_age_data(df):
    olympics = df
    # Remove White Space
    olympics.weight = olympics.weight.str.rstrip()
    # Conver 'na' to NaN
    olympics.height = olympics.height.replace('na',np.NaN)
    olympics.weight = olympics.weight.replace('na',np.NaN)
    # Convert Height/Weight to numeric
    olympics['height']=pd.to_numeric(olympics['height'])
    olympics['weight']=pd.to_numeric(olympics['weight'])
    # Event year to datetime
    olympics['born'] = pd.to_datetime(olympics['born'], format="%Y-%m-%d")
    olympics['event_year'] = pd.to_datetime(olympics['event_year'], format="%Y")
    # Convert Yearborn to just year
    olympics['year_born']=olympics['born'].dt.year
    olympics['year_born'] = pd.to_datetime(olympics['year_born'], format="%Y")
    # Convert event year to integer
    #olympics['event_year'].astype(str).astype(int)
    # Convert age from days to years
    olympics['age']=(olympics.event_year-olympics.year_born).astype('timedelta64[Y]')
    # Calculate BMI
    olympics['bmi'] = (olympics.weight / (olympics.height**2))*10000
    # Find Means
    mean_age=olympics['age'].mean()
    mean_height = olympics['height'].mean()
    mean_weight = olympics['weight'].mean()
    #Fill nulls with means
    olympics['height'].fillna(value=mean_height, inplace=True)
    olympics['weight'].fillna(value=mean_weight, inplace= True)
    olympics['age'].fillna(value=mean_age, inplace=True)
    olympics['bmi'] = (olympics.weight / (olympics.height**2))*10000
    # Delete born after age is generated
    olympics = olympics.drop(['born','year_born'], axis=1)
    
    return olympics