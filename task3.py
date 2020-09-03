import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df=pd.read_csv(r'./tempYearly.csv')
sns.set(rc={'figure.figsize':(12,6)})
sns.scatterplot(x='Year',y='Temperature',data=df)
plt.show()

sns.regplot(x='Rainfall',y='Temperature',data=df)
plt.show()