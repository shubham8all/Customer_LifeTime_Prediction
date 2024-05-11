import streamlit as st
import pandas as pd
import lifetimes
import math
import string
import numpy as np
import xlrd
import datetime
np.random.seed(42)
import altair as alt
import time
import warnings
warnings.filterwarnings("ignore")
from math import sqrt
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from lifetimes.plotting import plot_frequency_recency_matrix
from lifetimes.plotting import plot_probability_alive_matrix
from lifetimes.plotting import plot_period_transactions
from lifetimes.utils import calibration_and_holdout_data
from lifetimes import ParetoNBDFitter
from lifetimes.plotting import plot_history_alive
from sklearn.metrics import mean_squared_error, r2_score


st.markdown(""" # Customer Lifetime Prediction App


Upload the RFM data and get your customer lifetime prediction on the fly !!! :smile:

	""")