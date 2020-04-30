import os
import pandas as pd
from pandas import isnull


# JOINING COLUMNS
#default join will be inner
#pd.merge(dataframe1, dataframe2, left_on='playerId', right_on='plrId', how='left')
#left_index=True