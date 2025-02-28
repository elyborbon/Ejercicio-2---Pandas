import pandas as pd

datos = [2,3,5,7,11]
serie = pd.Series (datos)
print (serie)
print (serie.size)
print (serie.describe())