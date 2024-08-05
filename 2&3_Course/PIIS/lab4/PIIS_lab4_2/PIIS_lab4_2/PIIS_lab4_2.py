import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

# Importing the dataset
data = pd.read_csv("data.csv")
# Dropping the Unnamed: 32 and the id column since these do not provide any useful information for our models.
data.drop(['Unnamed: 32', 'id'], axis=1, inplace=True)
# Spliting target variable and independent variables
X = data.drop(['diagnosis'], axis = 1)
y = data['diagnosis']
# Split on training and test sets
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.20,random_state = 42)
# Ensemble of Models
estimator = []
estimator.append(('LR', LogisticRegression(solver ='lbfgs',multi_class ='multinomial',max_iter = 5000)))
estimator.append(('SVC', SVC(gamma ='auto', probability = True)))
estimator.append(('DTC', DecisionTreeClassifier()))
print(estimator)

from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score
# Voting Classifier with hard voting
hard_voting = VotingClassifier(estimators = estimator, voting ='hard')
hard_voting.fit(X_train, y_train)
y_pred = hard_voting.predict(X_test)
# accuracy_score metric to predict Accuracy
score = accuracy_score(y_test, y_pred)
print("Hard Voting Score", score)

# Voting Classifier with soft voting
soft_voting = VotingClassifier(estimators = estimator, voting ='soft')
soft_voting.fit(X_train, y_train)
y_pred = soft_voting.predict(X_test)
# Using accuracy_score
score = accuracy_score(y_test, y_pred)
print("Soft Voting Score", score)

from sklearn.datasets import make_blobs
from matplotlib import pyplot
from pandas import DataFrame
# generate 2d classification dataset
X, y = make_blobs(n_samples=500, centers=3, n_features=2, cluster_std=2, random_state=2)
# scatter plot, dots colored by class value
df = DataFrame(dict(x=X[:,0], y=X[:,1], label=y))
colors = {0:'red', 1:'blue', 2:'green'}
fig, ax = pyplot.subplots()
grouped = df.groupby('label')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='x', y='y', label=key, color=colors[key])
pyplot.show()

import numpy as np
# Importing the dataset
data = pd.read_csv("data.csv")
# Dropping the Unnamed: 32 and the id column since these do not provide any useful information for our models.
data.drop(['Unnamed: 32', 'id'], axis=1, inplace=True)
# Spliting target variable and independent variables
X = data.drop(['diagnosis'], axis = 1)
y = data['diagnosis']
# Split on training and test sets
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.20,random_state = 42)
lr = LogisticRegression(solver ='lbfgs',multi_class ='multinomial',max_iter = 5000)
sv = SVC(gamma ='auto', probability = True)
dt = DecisionTreeClassifier()
# encoding
y_train = [0 if elem=='B' else 1 for elem in y_train]
lr.fit(X_train, y_train)
sv.fit(X_train, y_train)
dt.fit(X_train, y_train)
predicted = [lr.predict(X_test), sv.predict(X_test), dt.predict(X_test)]
best_weights = []
best_accuracy = 0
# Optimal wages
for w1 in np.arange(0.05, 0.95, 0.05):
    for w2 in np.arange(0.1, 0.95, 0.05):
        if w1+w2>0.95:
            continue
        else:
            w3 = 1-(w1+w2)
            y_pred = [predicted[0][i]*w1 + predicted[1][i]*w2 + predicted[2][i]*w3 for i in range(len(y_test))]
            # decoding
            y_pred = ['B' if round(elem)==0 else 'M' for elem in y_pred]
            score = accuracy_score(y_test, y_pred)
            if score>best_accuracy:
                best_accuracy = score
                best_weights = [w1, w2, w3]
print(f'Best weights = {[round(x, 2) for x in best_weights]}, Best accuracy = {round(best_accuracy, 3)}')

from sklearn.datasets import load_wine
from sklearn.neighbors import KNeighborsClassifier
# define dataset
X,y = load_wine().data,load_wine().target
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=1)
X_train, X_val, y_train, y_val = train_test_split(
X_train, y_train, test_size=0.25, random_state=1)
x_val=pd.DataFrame(X_val)
x_test=pd.DataFrame(X_test)
model1 = DecisionTreeClassifier()
model1.fit(X_train, y_train)
val_pred1=model1.predict(X_val)
test_pred1=model1.predict(X_test)
val_pred1=pd.DataFrame(val_pred1)
test_pred1=pd.DataFrame(test_pred1)
model2 = KNeighborsClassifier()
model2.fit(X_train,y_train)
val_pred2=model2.predict(X_val)
test_pred2=model2.predict(X_test)
val_pred2=pd.DataFrame(val_pred2)
test_pred2=pd.DataFrame(test_pred2)
df_val=pd.concat([x_val, val_pred1,val_pred2],axis=1)
df_test=pd.concat([x_test, test_pred1,test_pred2],axis=1)
model = LogisticRegression()
model.fit(df_val,y_val)
print('Blending accuracy: ', model.score(df_test,y_test))

from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, BaggingClassifier
from sklearn.linear_model import RidgeClassifier
from sklearn.model_selection import cross_val_score
# define dataset
X,y = load_wine().data,load_wine().target
# Create classifiers
rf = RandomForestClassifier()
et = ExtraTreesClassifier()
knn = KNeighborsClassifier()
svc = SVC()
rg = RidgeClassifier()
clf_array = [rf, et, knn, svc, rg]
for clf in clf_array:
    vanilla_scores = cross_val_score(clf, X, y, cv=10, n_jobs=-1)
    bagging_clf = BaggingClassifier(clf,max_samples=0.4, max_features=10, random_state=42)
    bagging_scores = cross_val_score(bagging_clf, X, y, cv=10,n_jobs=-1)
    print ("Mean of: {1:.3f}, std: (+/-) {2:.3f} [{0}]".format(clf.__class__.__name__,vanilla_scores.mean(), vanilla_scores.std()))
    print ("Mean of: {1:.3f}, std: (+/-) {2:.3f} [Bagging {0}]\n".format(clf.__class__.__name__,bagging_scores.mean(), bagging_scores.std()))

from sklearn.datasets import load_wine
# define dataset
X,y = load_wine().data,load_wine().target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
print(X_train.shape, X_test.shape)

from sklearn.ensemble import AdaBoostClassifier
ada_boost = AdaBoostClassifier(random_state=1)
ada_boost.fit(X_train, y_train)
print('AdaBoost accuracy: ', ada_boost.score(X_test,y_test))

from sklearn.ensemble import GradientBoostingClassifier
grad_boost= GradientBoostingClassifier(learning_rate=0.01,random_state=1)
grad_boost.fit(X_train, y_train)
print('Gradient Boost accuracy: ', grad_boost.score(X_test,y_test))

import xgboost as xgb
xgb_boost=xgb.XGBClassifier(random_state=1,learning_rate=0.01)
xgb_boost.fit(X_train, y_train)
print('Extreme Gradient Boost accuracy: ', xgb_boost.score(X_test,y_test))
