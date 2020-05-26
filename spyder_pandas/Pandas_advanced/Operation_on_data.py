import os
import pandas as pd
from pandas import isnull


# JOINING COLUMNS
#default join will be inner
#pd.merge(dataframe1, dataframe2, left_on='playerId', right_on='plrId', how='left')
#left_index=True
#to chceck validate option 1:m one to many, m:m many to many, 1:1 one to one
#like in join

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
master = pd.read_csv(os.path.join(BASE_PATH,'output','Cleared_master.csv'))
scoring = pd.read_csv(os.path.join(BASE_PATH,'output','Cleared_scoring.csv'))
teams = pd.read_csv(os.path.join(BASE_PATH,'output','Cleared_teams.csv'))
teamsSplit = pd.read_csv(os.path.join(BASE_PATH,'output','Cleared_teams_splits.csv'))


master_scoring = pd.merge(master, scoring, left_index=True, right_on="playerID")