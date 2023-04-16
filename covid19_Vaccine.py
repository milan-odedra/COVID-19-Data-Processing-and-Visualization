# Import Libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# read data into pandas
df=pd.read_csv('country_vaccinations.csv')

# prints first five columns of dataset
print(df.head())

# prints missing values
print(df.isnull().sum())