# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 01:13:05 2018

@author: jenny
"""

import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
#拟合数据
clf.fit(X, Y)
print ("==使用predict进行预测的结果==")
print(clf.predict([[-0.8, -1]]))
print ("==使用predict_proba进行预测的结果===")
print(clf.predict_proba([[-0.8, -1]]))
print ("==使用predict_log_proba进行预测的结果==")
print(clf.predict_log_proba([[-0.8, -1]]))