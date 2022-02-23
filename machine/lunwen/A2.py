import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import Normalizer
from sklearn.metrics import (precision_score, recall_score,f1_score, accuracy_score,mean_squared_error,mean_absolute_error, roc_curve, classification_report,auc)
from sklearn.preprocessing import LabelEncoder

traindata=pd.read_csv('D:/Users/yangsong/PycharmProjects/pythonProject2/machine/lunwen/UNSW_NB15_training-set.csv',skiprows=1,names=['id','dur','proto','service','state','spkts','dpkts','sbytes','dbytes','rate','sttl','dttl','sload','dload','sloss','dloss','sinpkt','dinpkt','sjit','djit','swin','stcpb','dtcpb','dwin','tcprtt','synack','ackdat','smean','dmean','trans_depth','response_body_len','ct_srv_src','ct_state_ttl','ct_dst_ltm','ct_src_dport_ltm','ct_dst_sport_ltm','ct_dst_src_ltm','is_ftp_login','ct_ftp_cmd','ct_flw_http_mthd','ct_src_ltm','ct_srv_dst','is_sm_ips_ports','attack_cat','label'])
testdata=pd.read_csv('D:/Users/yangsong/PycharmProjects/pythonProject2/machine/lunwen/UNSW_NB15_training-set.csv',skiprows=1,names=['id','dur','proto','service','state','spkts','dpkts','sbytes','dbytes','rate','sttl','dttl','sload','dload','sloss','dloss','sinpkt','dinpkt','sjit','djit','swin','stcpb','dtcpb','dwin','tcprtt','synack','ackdat','smean','dmean','trans_depth','response_body_len','ct_srv_src','ct_state_ttl','ct_dst_ltm','ct_src_dport_ltm','ct_dst_sport_ltm','ct_dst_src_ltm','is_ftp_login','ct_ftp_cmd','ct_flw_http_mthd','ct_src_ltm','ct_srv_dst','is_sm_ips_ports','attack_cat','label'])
for column in traindata.columns:
    if traindata[column].dtype == type(object):
        le = LabelEncoder()  #标签编码,即是对不连续的数字或者文本进行编号,转换成连续的数值型变量
        traindata[column] = le.fit_transform(traindata[column])

for column in testdata.columns:
    if testdata[column].dtype == type(object):
        le = LabelEncoder()
        testdata[column] = le.fit_transform(testdata[column])
X1 = traindata.iloc[:,1:44]
Y1 = traindata.iloc[:,44]
Y2 = testdata.iloc[:,44]
X2 = testdata.iloc[:,1:44]

scaler = Normalizer().fit(X1)
trainX = scaler.transform(X1)
scaler = Normalizer().fit(X2)
testT = scaler.transform(X2)
traindata = np.array(trainX)
trainlabel = np.array(Y1)

testdata = np.array(testT)
testlabel = np.array(Y2)
model = DecisionTreeClassifier()  #决策树
model.fit(traindata, trainlabel)
expected = testlabel
predicted = model.predict(testdata)
accuracy = accuracy_score(expected, predicted)
recall = recall_score(expected, predicted, average="binary")
precision = precision_score(expected, predicted , average="binary") #精确率
f1 = f1_score(expected, predicted , average="binary")
cm = metrics.confusion_matrix(expected, predicted)
print(cm,cm[0][0],cm[0][1])  #混淆矩阵
tpr = float(cm[0][0])/np.sum(cm[0])
fpr = float(cm[1][1])/np.sum(cm[1])
print("%.3f" %tpr)
print("%.3f" %fpr)
print("Accuracy","%.3f" %accuracy)
print("precision","%.3f" %precision)
print("recall","%.3f" %recall)
print("f-score","%.3f" %f1)
print("fpr","%.3f" %fpr)
print("tpr","%.3f" %tpr)
