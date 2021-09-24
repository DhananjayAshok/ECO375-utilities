import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def line(dataset, X, y, order=1):
    sns.regplot(x=X, y=y, data=dataset.data, order=order, line_kws={"color": "red"})
    plt.title(f"Line Plot {X} vs {y} from {dataset.name} dataset")
    plt.xlabel(f"{y}")
    plt.ylabel(f"{X}")
    plt.show()


def scatter(dataset, X, y, line_param_results=None):
    sns.scatterplot(x=X, y=y, data=dataset.data)
    if line_param_results is not None:
        x_min = min(dataset.data[X])
        x_max = max(dataset.data[X])
        xs = np.linspace(x_min, x_max, num=100)
        coef = line_param_results.params[X]
        intercept = line_param_results.params['const']
        preds = (xs * coef) + intercept
        plt.plot(xs, preds, color="r")
    plt.title(f"Scatter Plot {X} vs {y} from {dataset.name} dataset")
    plt.xlabel(f"{y}")
    plt.ylabel(f"{X}")
    plt.show()