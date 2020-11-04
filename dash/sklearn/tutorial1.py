import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

train_url = "https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/train.csv"
train_df = pd.read_csv(train_url)

test_url = "https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/test.csv"
test_df = pd.read_csv(test_url)

train_length = len(train_df)
test_col = len(test_df.columns)

description = train_df.describe()
print(description)

prop_area_count = train_df['Property_Area'].value_counts()
print(prop_area_count)

train_df['LoanAmount'].hist()