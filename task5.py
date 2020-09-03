import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv(r'./tempYearly.csv')
sns.jointplot("Rainfall","Temperature",data=df,kind="reg")
plt.show()