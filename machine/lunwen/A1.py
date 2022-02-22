import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('F:/个人/学校/学习资料/UNSW-NB15 - CSV Files/a part of training and testing set/UNSW_NB15_training-set.csv')
plt.figure((figsize=(10, 16)))
sns.heatmap(data.corr(),annot=True,cmap='RdYlGn',linewidths=0.2) #data.corr()-->correlation matrix
fig=plt.gcf()
fig.set_size_inches(10000,8000)
plt.show()