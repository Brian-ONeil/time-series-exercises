### imports

import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

import warnings
warnings.filterwarnings("ignore")

import acquire as acq

### functions

def prep_ts_superstore(df):
    '''takes in ts_superstore df and returns prepped version'''
    
    #load my csv
    df = pd.read_csv('ts_superstore.csv', skiprows=1, index_col=0)
    
    #convert date column to datetime format and strip
    df.sale_date = df.sale_date.str.replace(' 00:00:00 GMT', '')
    df.sale_date = df.sale_date.str.strip()
    df.sale_date = pd.to_datetime(df.sale_date, format = '%a, %d %b %Y')
    
    #set index to sale_date and sort it
    df = df.set_index('sale_date')
    df = df.sort_index()
    
    # Add month column
    df['month'] = df.index.month

    # Add day of week column
    df['day_of_week'] = df.index.dayofweek
    
    # Add year column
    df['year'] = df.index.year
    
    # Add sales_total column
    df['sales_total'] = df['sale_amount'] * df['item_price']
    
    return df


def prep_germ_df(df):
    '''acquires germany data, preps it, and returns germ_df'''
    
    germ_df = acq.get_germany_data()
    
    #converts datetime format
    germ_df.index = pd.to_datetime(germ_df.index)
    
    #adds month and a year colum to df
    germ_df['Month'] = germ_df.index.month
    germ_df['Year'] = germ_df.index.year
    
    #removes nulls from 'Wind' and 'Solar' column and adds "0"
    germ_df['Wind'] = germ_df['Wind'].fillna(0)
    germ_df['Solar'] = germ_df['Solar'].fillna(0)
    
    #adds wind and solar to the 'wind+solar column'
    germ_df['Wind+Solar'] = germ_df['Wind+Solar'].fillna(germ_df['Wind'] + germ_df['Solar'])
    
    #changes all features to lower case
    germ_df.columns = germ_df.columns.str.lower()
    
    return germ_df
