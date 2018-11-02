# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 23:01:21 2018

@author: jenny
"""
class NBClassify(object):
    def __init__(self, fillNa = 1):
        self.fillNa = 1

    def train(self, trainSet):
        # 计算每种类别的概率
        
        dictTag = {}
        # 保存所有标签的所有种类，以及这些标签出现的次数
        for subTuple in trainSet:
            dictTag[str(subTuple[1])] = 1 if str(subTuple[1]) not in dictTag.keys() else dictTag[str(subTuple[1])] + 1
        #print(dictTag)
        # 保存每个标签本身的概率
        tagProbablity = {}
        # 计算所有标签之和
        totalFreq = sum([value for value in dictTag.values()])
        #计算每一个标签的出现概率,先验概率
        for key, value in dictTag.items():
          tagProbablity[key] = value / totalFreq
        #print(tagProbablity)
        self.tagProbablity = tagProbablity
        ##############################################################################
        # 计算特征的条件概率
        # 保存特征属性的基本信息
        dictFeaturesBase = {}
        for subTuple in trainSet:
            #统计输入样本的职业出现的次数和症状出现的次数
            for key, value in subTuple[0].items():
                if key not in dictFeaturesBase.keys():
                    dictFeaturesBase[key] = {value:1}
                else:
                    if value not in dictFeaturesBase[key].keys():
                        dictFeaturesBase[key][value] = 1
                    else:
                        dictFeaturesBase[key][value] += 1
        #print(dictFeaturesBase)
        # dictFeaturesBase = {
          # '职业': {'农夫': 1, '教师': 2, '建筑工人': 2, '护士': 1},
          # '症状': {'打喷嚏': 3, '头痛': 3}
          # }
        #由病情：职业、症状构造一个新的字典结构，以结果做为键
        dictFeatures = {}.fromkeys([key for key in dictTag])
        for key in dictFeatures.keys():
          dictFeatures[key] = {}.fromkeys([key for key in dictFeaturesBase])
        for key, value in dictFeatures.items():
          for subkey in value.keys():
            value[subkey] = {}.fromkeys([x for x in dictFeaturesBase[subkey].keys()])
        #print(dictFeatures)
        # dictFeatures = {
        #  '感冒 ': {'症状': {'打喷嚏': None, '头痛': None}, '职业': {'护士': None, '农夫': None, '建筑工人': None, '教师': None}},
        #  '脑震荡': {'症状': {'打喷嚏': None, '头痛': None}, '职业': {'护士': None, '农夫': None, '建筑工人': None, '教师': None}},
        #  '过敏 ': {'症状': {'打喷嚏': None, '头痛': None}, '职业': {'护士': None, '农夫': None, '建筑工人': None, '教师': None}}
        #  }
        # initialise dictFeatures
        for subTuple in trainSet:
          for key, value in subTuple[0].items():
            dictFeatures[subTuple[1]][key][value] = 1 if dictFeatures[subTuple[1]][key][value] == None else dictFeatures[subTuple[1]][key][value] + 1
        #print(dictFeatures)
        #dictFeatures={
        #   '脑震荡': {'症状': {'打喷嚏': None, '头痛': 2}, '职业': {'农夫': None, '建筑工人': 1, '教师': 1, '护士': None}}, 
        #   '感冒 ': {'症状': {'打喷嚏': 2, '头痛': 1}, '职业': {'农夫': None, '建筑工人': 1, '教师': 1, '护士': 1}}, 
        #   '过敏 ': {'症状': {'打喷嚏': 1, '头痛': None}, '职业': {'农夫': 1, '建筑工人': None, '教师': None, '护士': None}}}
        # 如果训练样本没有值，由None改为一个非常小的数值，表示其概率极小而并非是零
        for tag, featuresDict in dictFeatures.items():
          for featureName, featureValueDict in featuresDict.items():
            for featureKey, featureValues in featureValueDict.items():
              if featureValues == None:
                featureValueDict[featureKey] = self.fillNa

        #featureValueDict={'农夫': 1, '建筑工人': 1, '教师': 1, '护士': 1}
        # 由特征频率计算特征的条件概率P(feature|tag)
        #print(dictFeatures)
        #dictFeatures={
        # '过敏 ': {'症状': {'头痛': 1, '打喷嚏': 1}, 职业': {'农夫': 1, '建筑工人': 1, '护士': 1, '教师': 1}}, 
        # '感冒 ': {'症状': {'头痛': 1, '打喷嚏': 2}, '职业': {'农夫': 1, '建筑工人': 1, '护士': 1, '教师': 1}}, 
        # '脑震荡': {'症状': {'头痛': 2, '打喷嚏': 1}, '职业': {'农夫': 1, '建筑工人': 1, '护士': 1, '教师': 1}}}
        for tag, featuresDict in dictFeatures.items():
          for featureName, featureValueDict in featuresDict.items():
              totalCount = sum([x for x in featureValueDict.values() if x != None])
              for featureKey, featureValues in featureValueDict.items():
                  featureValueDict[featureKey] = featureValues/totalCount if featureValues != None else None
        self.featuresProbablity = dictFeatures
        #print(self.featuresProbablity)
        #featuresProbablity={'过敏 ': {'职业': {'护士': 0.25, '教师': 0.25, '农夫': 0.25, '建筑工人': 0.25}, '症状': {'头痛': 0.5, '打喷嚏': 0.5}}, 
        #                    '脑震荡': {'职业': {'护士': 0.25, '教师': 0.25, '农夫': 0.25, '建筑工人': 0.25}, '症状': {'头痛': 0.6666666666666666, '打喷嚏': 0.3333333333333333}}, 
         #                   '感冒 ': {'职业': {'护士': 0.25, '教师': 0.25, '农夫': 0.25, '建筑工人': 0.25}, '症状': {'头痛': 0.3333333333333333, '打喷嚏': 0.6666666666666666}}}
    ##############################################################################
    def classify(self, featureDict):
        resultDict = {}
        # 计算每个标签tag的条件概率
        for key, value in self.tagProbablity.items():
            
          iNumList = []
          for f, v in featureDict.items():
            #print(f)
            if self.featuresProbablity[key][f][v]:
              iNumList.append(self.featuresProbablity[key][f][v])
          #print(iNumList,key)
          conditionPr = 1
          for iNum in iNumList:
              
              conditionPr *= iNum
              #print(iNum,conditionPr)
          resultDict[key] = value * conditionPr
        
        # 对比每个tag的条件概率的大小
        resultList = sorted(resultDict.items(), key=lambda x:x[1], reverse=True)
        print(resultList)
        return resultList[0][0]
if __name__ == '__main__':
    trainSet = [
        ({"症状":"打喷嚏", "职业":"护士"}, "感冒 "),
        ({"症状":"打喷嚏", "职业":"农夫"}, "过敏 "),
        ({"症状":"头痛", "职业":"建筑工人"}, "脑震荡"),
        ({"症状":"头痛", "职业":"建筑工人"}, "感冒 "),
        ({"症状":"打喷嚏", "职业":"教师"}, "感冒 "),
        ({"症状":"头痛", "职业":"教师"}, "脑震荡"),
      ]
    monitor = NBClassify()
    # trainSet is something like that [(featureDict, tag), ]
    monitor.train(trainSet)
    # 请问他最容易患上什么病？
    result = monitor.classify({"症状":"打喷嚏", "职业":"建筑工人"})
    print(result)