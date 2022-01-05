import cv2 as cv
import numpy
import time
from sklearn.feature_extraction import DictVectorizer

def dictvec():
    """
    字典数据特征抽取，向量化
    :return:
    """
    # 1 新建向量化器实例
    dic = DictVectorizer(sparse=False)  # sparse是否稀疏
    # 2 调用fit_transform方法，执行向量化
    data = dic.fit_transform([
        {'city': '北京', 'pos': '北方', 'temperature': 100},
        {'city': '上海', 'pos': '东方', 'temperature': 60},
        {'city': '深圳', 'pos': '南方', 'temperature': 30},
        {'city': '重庆', 'pos': '南方', 'temperature': 70},
    ])
    print(dic.get_feature_names())
    print(data)
    # ps: 反向量化，恢复成原始数据形式
    print(dic.inverse_transform(data)[0])

dictvec()
