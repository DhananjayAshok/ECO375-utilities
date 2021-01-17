import os
import pandas as pd

data_dir = "data"


class DataSet():
    def __init__(self, name, caps=False):
        self.name = name
        if caps:
            self.data = pd.read_stata(data_dir+f"/{name}.DTA")
        else:
            self.data = pd.read_stata(data_dir + f"/{name}.dta")

    def __str__(self):
        s0 = str(self.data.columns)
        s1 = str(self.data.head())
        s2 = str(self.data.describe())
        s3 = str(self.data.info())
        return "Columns: " + s0 + "\n" + s1 + "\n" + s2 + "\n" + s3

