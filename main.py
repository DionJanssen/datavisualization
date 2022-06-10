import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import plotly.express as px

df = pd.read_csv("owid-covid-data.csv")

# create barplot of total cases vs continent
sns.barplot(x="total_cases", y="continent", data=df)
# show plot
plt.show()

# group by continent and give observations
df.groupby("continent").total_cases.sum().plot(kind="bar")
plt.show()

# print(df_continent)

# sns.barplot(x="total_cases", y="continent", data=df_continent)