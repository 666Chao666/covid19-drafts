import pandas as pd
from os.path import join as oj
import os

def load_commute(data_dir='.'):
    ''' Load in commute data (4 .xlsx tables)

    Parameters
    ----------
    data_dir : str; path to the data directory of raw commute data

    Returns
    -------
    data frame
    '''

    for i in range(1, 5):
        raw = pd.read_excel(oj(data_dir, "table" + str() + ".xlsx"))

    return raw

if __name__ == '__main__':
    raw = load_ca_hospitalizations()
    print('loaded ca_hospitalizations successfully.')
