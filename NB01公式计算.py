import numpy as np
#打喷嚏：1，头痛：2，护士：3，工人：4，教师：5，农夫：6，感冒：7，过敏：8，脑震荡：9
trainSet = [
        ({"症状":1, "职业":3}, 7),
        ({"症状":1, "职业":6}, 8),
        ({"症状":2, "职业":4}, 9),
        ({"症状":2, "职业":4}, 7),
        ({"症状":1, "职业":5}, 7),
        ({"症状":2, "职业":5}, 9),
      ]
from pandas import DataFrame
from sklearn.naive_bayes import GaussianNB


x=np.array([i[1] for i in trainSet])
list_shu=[]
for i in trainSet:
    list_shu.append([j for h,j in i[0].items()])
y=np.array(list_shu)
clf=GaussianNB()
clf.fit(y,x)
print(clf.predict([[1,4]]))
