# encoding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 读取文件
data = pd.read_csv('D:/Users/yangsong/PycharmProjects/pythonProject2/machine/titanic/train.csv')
# 查看前几行
# print(data.head())
# # 查看缺失值
# print(data.isnull().sum())
# # 表格数据统计
# print(data.describe())
# plt测试
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='An Example Axes',
#        ylabel='Y-Axis', xlabel='X-Axis')
# plt.show()
# 以..为基准统计指标
# 先按照a进行分组，再按照b进行分组，最后将b进行叠加
print(data.groupby(['Sex','Survived'])['Survived'].count())
# print(data.groupby(['MATE30','no'])['MATE30'].count())

data.isnull().sum()
# print(data.describe())

# 获救比例
# 创建1*2个统计图
# f, ax = plt.subplots(1,3,figsize=(18,8))
# data['Survived'].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%',ax=ax[0],shadow=True)
# ax[0].set_title('Survived')
# ax[0].set_ylabel('')
#
# # 以Sur..为数据画柱状图
# sns.countplot('Survived',data=data,ax=ax[1])
# ax[1].set_title('Survived2')
# plt.show()
#
# f, ax = plt.subplots(1,2,figsize=(18,8))
# data[['Sex','Survived']].groupby(['Sex']).mean().plot.bar(ax = [0])
# ax[0].set_title('Survived and sex')
# sns.countplot('Sex',hue='Survived',data = data, ax = ax[1])
# ax[1].set_title('Sex:Survived vs Dead')
# plt.show()

# 表格
# pd.crosstab(data.Pclass,data.Survived,margins=True)
#根据船舱
# f,ax=plt.subplots(1,2,figsize=(18,8))
# data['Pclass'].value_counts().plot.bar(color=['#CD7F32','#FFDF00','#D3D3D3'],ax=ax[0])
# ax[0].set_title('Number Of Passengers By Pclass')
# ax[0].set_ylabel('Count')
# sns.countplot('Pclass',hue='Survived',data=data,ax=ax[1])
# ax[1].set_title('Pclass:Survived vs Dead')
# plt.show()

# 根据船舱以外再加性别
# print(pd.crosstab([data.Sex,data.Survived],data.Pclass,margins=True))

# 两个指标对应一个结果 hue轴
# sns.factorplot('Pclass','Survived',hue='Sex',data=data)
# plt.show()

# age连续值特征对结果的影响 最大值 最小值 平均值
# print('Oldest Passenger was of:',data['Age'].max(),'Years')
# print('Youngest Passenger was of:',data['Age'].min(),'Years')
# print('Average age on the ship:',data['Age'].mean(),'Years')

#小提琴图（violinplot）
f,ax = plt.subplots(1,2,figsize=(18,8))
sns.violinplot('Pclass','Age',hue='Survived' ,data=data ,split=True, ax=ax[0])
ax[0].set_title('Pclass and Age vs Survived')
ax[0].set_yticks(range(0,110,10))
sns.violinplot('Sex','Age',hue='Survived',data=data,split=True,ax=ax[1])
ax[0].set_title('Sex and Age vs Survived')
ax[0].set_yticks(range(0,110,10))
plt.show()