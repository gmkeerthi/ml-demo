# -*- coding: utf-8 -*-
"""Untitled31.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1v8s_d8Y8OhOp9d7vpuZuO068RtU70N_S
"""

import matplotlib.pyplot as plt
from sklearn import linear_model

height = [[4.0], [5.0], [6.0], [7.0], [8.0], [9.0], [10.0], [11.0]]
weight = [8, 10, 12, 14, 16, 20, 22, 24]

plt.scatter(height, weight, color='black')
plt.xlabel("height")
plt.ylabel("weight")

reg = linear_model.LinearRegression()
reg.fit(height, weight)

X_height = [[12.0]]
print(reg.predict(X_height))  # Ensure there's only one newline below this line
