import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

pd.options.mode.chained_assignment = None

def create_DataFrame() -> pd.DataFrame:
    """This function takes data from 2 csv files and create dataframe with 2 columns"""
    df1 = pd.read_csv(
        os.path.join("/Users", "79276", "Desktop", "Lab4Sem3", "annotationleopard.csv"), 
                      sep=',',
                      header=None)
    df2 = pd.read_csv(
        os.path.join("/Users", "79276", "Desktop", "Lab4Sem3", "annotationtiger.csv"), sep=',',
        header=None)
    df = pd.concat([df1, df2], ignore_index=True)
    df.drop(1, axis=1, inplace=True)
    df.rename(columns={0: 'absolute_path', 2: 'dataset_class'}, inplace=True)
    return df


def add_mark(df: pd.DataFrame) -> None:
    """This function adds third column in dataframe - mark of image(1 or 0)"""
    value = []
    for item in df['dataset_class']:
        if item == 'tiger':
            value.append(0)
        else:
            value.append(1)
    df['mark'] = value