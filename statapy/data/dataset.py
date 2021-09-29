import os
import pandas as pd
from statapy.utils import column_corrector


class DataSet(object):
    """
    Class to hold a pandas dataset under the data field.

    """
    def __init__(self, name, filename="", url="", data=None):
        """

        :param name: Name of the DataSet object
        :param filename: path to file to be read in (supports csv and dta formats)
        :param url: url of csv to read
        :param data: dataFrame to serve as data value in case special loading is required
        """
        self.name = name
        if data is not None:
            self.data = data
            return

        if not os.path.exists(filename) and url == "":
            raise ValueError("File does not exists and url not specified")
        elif os.path.exists(filename):
            if len(filename) < 5:
                raise ValueError(f"Filename {filename} does not have length at least 5 and "
                                 f"hence cannot be a valid CSV/DTA")
            else:
                if filename[-3:] == "dta":
                    self.data = pd.read_stata(filename)
                elif filename[-3:] == "csv":
                    self.data = pd.read_csv(filename)
                else:
                    raise ValueError(f"Extension {filename[-3:]} not supported")
        else:
            self.data = pd.read_csv(url)
        self.original_columns = self.data.columns
        return

    def __str__(self):
        return f"Dataset {self.name}"

    def __repr__(self):
        return str(self)

    @column_corrector
    def report(self, columns=None):
        """
        Reports basic statistics on columns of dataset

        :param columns: List of columns to report on from dataset
        :return: None
        """
        df = self.data[columns]
        a = df.describe()
        b = df.info()
        print(a)
        print(b)
        return

    @column_corrector
    def make_dummies(self, columns=None):
        """

        :param columns: List of columns to be made into dummies
        :return: list of new columns (dummy columns) added to the dataset in this call
        """
        old_cols = set(self.data.columns)
        self.data = pd.get_dummies(self.data, columns=columns)
        now_cols = set(self.data.columns)
        new_cols = now_cols.difference(old_cols)
        return list(new_cols)

    @column_corrector
    def dropna(self, columns=None):
        """
        Drop rows which have an NA element in columns indicated by the slice
        :return:
        """
        self.data.dropna(inplace=True, subset=columns)









