import pandas as pd
import numpy as np
import plotly.express as px
import os
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler


xtrain, xtest, ytrain, ytest=train_test_split(X, y, test_size=0.2)