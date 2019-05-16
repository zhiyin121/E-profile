import numpy as np
from numpy import dot


class L_classifier:
    def __init__(self, labels):
        self.labels = labels
        self.w = []

    def train(self, corpus):
        for label in range(self.labels):
            labels = []
            vectors = []
            for inst in range(len(corpus.text)):
                feature = corpus.text[inst].feature_extraction(corpus.tf_idf)
                labels.append(corpus.gold[inst][label])
                vectors.append(feature2vector(feature))
            self.w.append(perceptron(vectors, labels))

    def predict(self, corpus):
        predict = []
        for inst in range(len(corpus.text)):
            labels = []
            for label in range(self.labels):
                if dot(self.w[label], feature2vector(corpus.text[inst].feature_extraction(corpus.tf_idf))) >= 0:
                    labels.append(1)
                else:
                    labels.append(0)
            predict.append(labels)
        return predict


def perceptron(features, labels):
    w = np.array([0] * len(features[0]))
    flag = False
    count = 0
    while not flag and count < 100:
        for i in range(len(features)):
            t = dot(features[i], w)
            if t <= 0 and labels[i] == 1:
                w += features[i]
                flag = False
                break
            if t >= 0 and labels[i] == 0:
                w -= features[i]
                flag = False
                break
            flag = True
        count += 1
    return w


def feature2vector(feature):
    vector = []
    for elem in feature:
        if feature[elem] is True:
            vector.append(1)
        else:
            vector.append(-1)
    return vector

