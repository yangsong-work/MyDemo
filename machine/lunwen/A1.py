import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression #logistic regression
from sklearn import svm #support vector Machine
from sklearn.ensemble import RandomForestClassifier #Random Forest
from sklearn.neighbors import KNeighborsClassifier #KNN
from sklearn.naive_bayes import GaussianNB #Naive bayes
from sklearn.tree import DecisionTreeClassifier #Decision Tree
from sklearn.model_selection import train_test_split #training and testing data split
from sklearn import metrics #accuracy measure
from sklearn.metrics import confusion_matrix #for confusion matrix

data = pd.read_csv('D:/Users/yangsong/PycharmProjects/pythonProject2/machine/lunwen/UNSW_NB15_training-set.csv')
# data = pd.read_csv('D:/Users/PycharmProjects/pyproject/machine/lunwen/UNSW_NB15_training-set.csv')
# plt.figure((figsize=(10, 16)))
# sns.heatmap(data.corr(),annot=True,cmap='RdYlGn',linewidths=0.1,annot_kws={'size':5}) #data.corr()-->correlation matrix
# fig=plt.gcf()
# fig.set_size_inches(10000,8000)
# plt.show()

train,test=train_test_split(data,test_size=0.3,random_state=0,stratify=data['label'])
train_X=train[train.columns[1:]]
train_Y=train[train.columns[:1]]
test_X=test[test.columns[1:]]
test_Y=test[test.columns[:1]]
X=data[data.columns[1:]]
Y=data['label']

model=svm.SVC(kernel='rbf',C=1,gamma=0.1)
model.fit(train_X,train_Y)
prediction1=model.predict(test_X)
print('Accuracy for rbf SVM is ',metrics.accuracy_score(prediction1,test_Y))