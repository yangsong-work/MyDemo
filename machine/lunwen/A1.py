import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('F:/个人/学校/学习资料/UNSW-NB15 - CSV Files/UNSW-NB15_4.csv')
sns.heatmap(data.corr(),annot=True,cmap='RdYlGn',linewidths=0.2) #data.corr()-->correlation matrix
fig=plt.gcf()
fig.set_size_inches(500,400)
plt.show()