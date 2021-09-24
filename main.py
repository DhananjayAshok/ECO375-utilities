from statapy.data.dataset import DataSet
from statapy.regression import *
from statapy.plotting import *

url = "https://www.stata.com/examples/auto.csv"
filename = "data/alcohol.dta"
dataset = DataSet(name="Sample", filename=filename)
df = dataset.data

