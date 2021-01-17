from dataset import DataSet
from regression import linear_regression
from plotting import line, scatter


def full_process(dataset, x, y):
    res = linear_regression(dataset, [x], y)
    scatter(dataset, x, y, res)
    return