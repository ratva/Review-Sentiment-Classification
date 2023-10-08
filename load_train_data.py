import numpy as np
import pandas as pd
import os

def load_data(x_data, y_data):
    data_dir = 'data_reviews'
    x_df = pd.read_csv(os.path.join(data_dir, x_data))
    y_df = pd.read_csv(os.path.join(data_dir, y_data))
    N, n_cols = x_df.shape
    # print("Shape of x_df: (%d, %d)" % (N,n_cols))
    # print("Shape of y_df: %s" % str(y_df.shape))
    # print(type(x_df))
    # print(type(y_df))
    # Print out the first five rows and last five rows
    text_list = x_df['text'].values.tolist()
    # print(text_list)
    return text_list