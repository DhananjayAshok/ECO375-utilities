import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
import numpy as np
from statapy.utils import save_fig_default, plotting_function


@plotting_function
def line(dataset, X, y, order=1, save_fig=save_fig_default):
    """
    Line plot of X vs y


    :param dataset: dataset object
    :param X: X column to plot
    :param y: y column to plot
    :param order:
    :param save_fig: True iff to save figure
    :return: None

    * function decorator changes output from function body
    """
    sns.regplot(x=X, y=y, data=dataset.data, order=order, line_kws={"color": "red"})
    title = f"Line Plot {X} vs {y} from {dataset.name} dataset"
    plt.title(title)
    plt.xlabel(f"{X}")
    plt.ylabel(f"{y}")
    plt.legend()
    return plt, title


@plotting_function
def scatter(dataset, X, y, line_param_results=None, save_fig=save_fig_default):
    """
    Scatterplot of X vs y

    :param dataset: dataset object
    :param X: X column to plot
    :param y: y column to plot
    :param line_param_results: result of a regression
    :param save_fig: True iff to save figure
    :return: None

    * function decorator changes output from function body
    """
    sns.scatterplot(x=X, y=y, data=dataset.data)
    if line_param_results is not None:
        x_min = min(dataset.data[X])
        x_max = max(dataset.data[X])
        xs = np.linspace(x_min, x_max, num=100)
        coef = line_param_results.params[X]
        intercept = line_param_results.params['const']
        preds = (xs * coef) + intercept
        plt.plot(xs, preds, color="r", label="Regression Line")
    title = f"Scatter Plot {X} vs {y} from {dataset.name} dataset"
    plt.title(title)
    plt.xlabel(f"{X}")
    plt.ylabel(f"{y}")
    plt.legend()
    return plt, title


@plotting_function
def bar(dataset, X, y, groupby=None, save_fig=save_fig_default):
    """
    Bar plot of X vs y

    :param dataset: dataset object
    :param X: X column to plot
    :param y: y column to plot
    :param groupby: Will group the X column observations by groupby column
    :param save_fig: True iff to save figure
    :return: None

    * function decorator changes output from function body
    """
    sns.barplot(x=X, y=y, data=dataset.data, hue=groupby, ci=95)
    title_add = f", grouped by {groupby}" if groupby is not None else ""
    title = f"Bar Plot {X} vs {y}{title_add} from {dataset.name} dataset"
    plt.title(title)
    plt.xlabel(f"{X}")
    plt.ylabel(f"{y}")
    plt.legend()
    return plt, title


@plotting_function
def dist(dataset, X, save_fig=save_fig_default):
    """
        Dist plot of X vs y

        :param dataset: dataset object
        :param X: X column to plot
        :param save_fig: True iff to save figure
        :return: None

        * function decorator changes output from function body
    """
    sns.displot(x=X, data=dataset.data)
    title = f"Dist Plot {X} from {dataset.name} dataset"
    plt.title(title)
    plt.xlabel(f"{X}")
    plt.legend()
    return plt, title


