# encoding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 读取文件
data = pd.read_excel('D://titanic//test.csv')
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
# print(data.groupby(['MATE30','no'])['no'].count())
# print(data.groupby(['MATE30','no'])['MATE30'].count())


f, ax = plt.subplots(1,2,figsize=(18,8))
data[['Sex','Survived']].groupby(['Sex']).mean().plot.bar(ax = [0])
ax[0].set_title('Survived and sex')
sns.countplot('Sex',hue='Survived',data = data, ax = ax[1])
ax[1].set_title('Sex:Survived vs Dead')
plt.show()