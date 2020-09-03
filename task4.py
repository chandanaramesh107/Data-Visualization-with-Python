import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv(r'./birthYearly.csv')
print(df)

data=df.pivot("month","year","births")
print(data)

sns.heatmap(data,annot=True,fmt="d")
plt.show()