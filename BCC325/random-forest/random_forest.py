# -*- coding: utf-8 -*-
"""random_forest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GhgrY6Z6OU5CKKq2DrkJrGmHdFNKNMi0
"""

import pandas as pd
from sklearn.datasets import load_digits
digits = load_digits()

dir(digits)

import matplotlib.pyplot as plt
plt.gray()
for index in range(4):
  plt.matshow(digits.images[index])

data_frame = pd.DataFrame(digits.data) #creates df just with DATA
data_frame

data_frame['target'] = digits.target #adding column TARGET to df
data_frame

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(data_frame.drop(['target'], axis='columns'), digits.target, test_size=0.2)
#uses the df without TARGET and digits with TARGET
#uses 20% to test

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()

model.verbose=1
model.fit(x_train, y_train)

model.score(x_test, y_test) #accuracy

y_predicted = model.predict(x_test)

from sklearn.metrics import confusion_matrix

confusion = confusion_matrix(y_test, y_predicted)
import matplotlib.pyplot as plt
import seaborn as sn

plt.figure(figsize=(10,7))
sn.heatmap(confusion, annot=True)
plt.xlabel('predicted')
plt.ylabel('truth')