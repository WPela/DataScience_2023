import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

from google.colab import drive  ## because I am using Google Colab and files saved on Google Drive
drive.mount('/content/drive')

xls = pd.ExcelFile('/content/drive/MyDrive/Python/Coal_CO2.xlsx')

df = pd.read_excel(xls, 'Final')
df.head()

x = df['Coal (Mt)']
y = df['Co2 (Mt)']

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

r2 = r ** 2

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.title("Linear regression (Coal - Co2) | R^2 = " + str(round(r2, 4)) + " | p value = " + str(round(p, 4)))
plt.xlabel("Coal (Mt)")
plt.ylabel("Co2 (Mt)")
plt.show()

pred = myfunc(200000)
pred
