#2025.04.30 파이썬 수업
#bmi 예측 머신러닝에서 객체지향실습

import numpy as np
from sklearn.cluster import mean_shift
from sklearn.metrics import mean_squared_error



np.random.seed(42)

height = np.random.normal(170,10,1000)
weight = np.random.normal(65,15,1000)
bmi = weight / (height / 100) **2

X = np.vstack((height, weight)).T
y = bmi

#데이터를 train용과 test용(30%)으로 나눔
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state= 42)

# 1. 함수를 이용한 머신러닝

'''
from p04bmifunctions import fit_decision_tree, predict_decision_tree

#학습 훈련 train
tree_model = fit_decision_tree(X_train, y_train, )
# 테스트 데이터로 예측
y_pred = predict_decision_tree(tree_model, X_test)
'''

# 2. 자체제작 클래스를 이용한 머신러닝
'''
from p04bmiclass import MyDecisionTree
tree = MyDecisionTree(3)
tree.fit(X_train, y_train)
y_pred = tree.predict(X_test)
'''

## 3. 남이 만들어놓은 클래스(DecisionTreeRegressor)를 이용한 머신러닝

from sklearn.tree import  DecisionTreeRegressor
tree = DecisionTreeRegressor()
tree.fit(X_train, y_train)
y_pred = tree.predict(X_test)




# 평가 : 예측된 결과와, 정답결과 비교
mse = mean_squared_error(y_pred, y_test)
print(f"평균제곱오차(MSE):{mse:.3f}")

# 일부 출력
for i in range(5):
    print(f"실제 BMI: {y_test[i]:.2f} | 예측 BMI: {y_pred[i]:.2f}")

