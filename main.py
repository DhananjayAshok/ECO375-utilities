from statapy.data.dataset import DataSet

url = "https://www.stata.com/examples/auto.csv"
filename = "data/alcohol.dta"
dataset = DataSet(name="Sample", filename=filename)
dataset.report()
df = dataset.data

