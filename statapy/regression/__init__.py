import statsmodels.api as sm
from statapy.utils import write_default, regression_function


@regression_function
def OLS_regression(dataset, X_cols=None, y_col=None, X=None, y=None, write=write_default):
    """
    Performs OLS Regression

    * X_cols and y_col must be specified with the argument name in the function call:
        e.g. linear_regression(dataset, X_cols=["variable_1"], y_col="outcome") is correct
             linear_regression(dataset, ["variable_1"], "outcome") is wrong


    :param dataset: dataset object
    :param X_cols: list of X columns to use
    :param y_col: target column
    :return: results object

    *params and returns are not as you'd expect from function body because of decorator
    """
    model = sm.OLS(y, X)
    results = model.fit()
    regtype = f"OLS"
    return results, regtype


