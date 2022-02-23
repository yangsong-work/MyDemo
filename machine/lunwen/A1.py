import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('D:/Users/yangsong/PycharmProjects/pythonProject2/machine/lunwen/UNSW_NB15_training-set.csv')
# plt.figure((figsize=(10, 16)))
sns.heatmap(data.corr(),annot=True,cmap='RdYlGn',linewidths=0.1,annot_kws={'size':5}) #data.corr()-->correlation matrix
fig=plt.gcf()
fig.set_size_inches(10000,8000)
plt.show()