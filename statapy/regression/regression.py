import statsmodels.api as sm


def linear_regression(dataset, X_cols, y_col):
    """

    :param dataset:
    :param X_cols:
    :param y_col:
    :return: tuple(fitted sklearn linear regression model, pandas dataFrame with coefficients and std for each
    """
    X = dataset.data[X_cols]
    y = dataset.data[y_col]
    X = sm.add_constant(X)
    print(X)
    model = sm.OLS(y, X)
    results = model.fit()
    print(results.summary())
    return results