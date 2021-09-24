from statapy.data.dataset import DataSet
from statapy.regression import *
from statapy.plotting import *

url = "https://stats.idre.ucla.edu/stat/data/hdp.csv"
dataset = DataSet(name="Sample", url=url)
X_cols = ["BMI", "tumorsize", "Age"]
y_col = "remission"

df = dataset.data

