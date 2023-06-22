from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

def get_csv_data(filepath):
     dataframe = pd.read_csv('/Users/tagline_145/Downloads/test.csv')
     return dataframe
     