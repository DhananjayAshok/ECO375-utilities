import statsmodels.api as sm
import os

log_path = "logs"
write_default = True
save_fig_default = True


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


def write_to_file(filename, msg):
    try:
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        with open(os.path.join(log_path, filename+".txt"), "w") as f:
            f.write(msg)
    except:
        print(f"Failed to write msg to filename: {filename}. Printing in console instead: \n {msg}")
    else:
        print(f"Log File: \"{os.path.join(log_path, filename+'.txt')}\" Succesfully Created")
    return


def get_dataset_sliced(dataset, X_cols, y_col):
    if X_cols is None or y_col is None:
        raise ValueError("X_cols and y_col cannot be None. "
                         "Please Ensure they were entered as explicit arguments with arg names")
    X_cols = get_column_sliced(dataset.data, X_cols)
    X = dataset.data[X_cols]
    y = dataset.data[y_col]
    X = sm.add_constant(X)
    return X, y


def regression_function(func):
    def r_func(*args, **kwargs):
        X_cols = kwargs.get("X_cols", None)
        y_col = kwargs.get("y_col", None)
        dataset = args[0]
        X, y = get_dataset_sliced(dataset, X_cols, y_col)
        filename = f"{dataset.name}-{X_cols} vs {y_col}"
        kwargs["X"] = X
        kwargs["y"] = y
        kwargs["X_cols"] = None
        kwargs["y_col"] = None
        write = kwargs.get("write", write_default)
        results, regtype = func(*args, **kwargs)
        msg = str(results.summary())
        filename = regtype + " " + filename
        if write:
            write_to_file(filename, msg)
        else:
            print(msg)
        return results
    return r_func


def save_plot(plt, title):
    save_path = os.path.join(log_path, f"{title}.png")
    plt.savefig(save_path)
    plt.clf()
    return


def plotting_function(func):
    def p_func(*args, **kwargs):
        plt, title = func(*args, **kwargs)
        save_fig = kwargs.get("save_fig", save_fig_default)
        if save_fig:
            save_plot(plt, title)
        else:
            plt.show()
        return
    return p_func


