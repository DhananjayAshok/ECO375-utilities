from statapy.regression.regression import linear_regression
from statapy.plotting.plotting import scatter


def full_process(dataset, x, y):
    res = linear_regression(dataset, [x], y)
    scatter(dataset, x, y, res)
    return