import pandas as pd


def get_column_sliced(data, columns):
    """

    :param data: DataFrame
    :param columns: Columns to select from DataFrame. May be None or empty or have columns out of datas columns
    :return: list of columns that are being selected from data
    """
    if columns is None or columns == []:
        return data.columns
    else:
        allcols = set(data.columns)
        pickedcols = set(columns)
        realcols = allcols.intersection(pickedcols)
        return list(realcols)


def column_corrector(func):
    def correct_func(*args, **kwargs):
        columns = kwargs.get("columns", None)
        data = kwargs.get("data", None)
        if data is None:
            try:
                data = args[0].data
            except IndexError:
                print("Something is wrong. Check the input to the column corrector decorator")
                return lambda x: x
        correct_columns = get_column_sliced(data, columns)
        kwargs["columns"] = correct_columns
        return func(*args, **kwargs)
    return correct_func
