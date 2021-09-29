import scipy.stats as stats


def mannwhitneyu(sample_0, sample_1, one_sided=False):
    """
    Performs the Mann-Whitney U test
    :param sample_0: array of values
    :param sample_1: array of values
    :param one_sided: True iff you want to use less than alternative hypothesis
    :return: statistic, pvalue
    """
    res = stats.mannwhitneyu(sample_0, sample_1, alternative="two-sided" if not one_sided else "less")
    return res.statistic, res.pvalue