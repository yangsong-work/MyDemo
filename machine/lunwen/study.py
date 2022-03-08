import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取数据
data = pd.read_csv('D:/Users/yangsong/PycharmProjects/pythonProject2/machine/lunwen/UNSW_NB15_training-set.csv')
# 查看数据结构
# 查看数据缺失值
print(data.isnull().sum())

# 查看被攻击的比例
f,ax=plt.subplots(1,2,figsize=(18,8))
data['label'].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%',ax=ax[0],shadow=True)
ax[0].set_title('label')
ax[0].set_ylabel('')
sns.countplot('label',data=data,ax=ax[1])
ax[1].set_title('label')
plt.show()




# 特征预处理

