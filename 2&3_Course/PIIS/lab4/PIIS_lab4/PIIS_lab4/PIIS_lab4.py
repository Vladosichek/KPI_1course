import pandas as pd
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

# Importing and prepearing
data = pd.read_csv("data.csv")
data.drop(['Unnamed: 32', 'id'], axis=1, inplace=True)
print("Size of data:", data.shape)
# Spliting target variable and independent variables
X = data.drop(['diagnosis'], axis = 1)
y = data['diagnosis']
# Splitting the data into training set and testset
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 0)
print("Size of training set:", X_train.shape)
print("Size of test set:", X_test.shape)

from sklearn.tree import DecisionTreeClassifier
# Create a Decision tree classifier model
clf = DecisionTreeClassifier()
default_params = clf.get_params()
# Train the model using the training sets
clf.fit(X_train, y_train)
# Prediction on test set
y_pred = clf.predict(X_test)
# Calculating the accuracy
acc_dt = metrics.accuracy_score(y_test, y_pred)
import warnings
# Turn off all warnings
warnings.filterwarnings("ignore")
# Create a Decision tree classifier model
clf = DecisionTreeClassifier()
# Hyperparameter Optimization
parameters = {'max_features': ['log2', 'sqrt','auto'],
'criterion': ['entropy', 'gini'],
'max_depth': [2, 3, 5, 10, 50],
'min_samples_split': [2, 3, 50, 100],
'min_samples_leaf': [1, 5, 8, 10]
}
# Run the grid search
grid_obj = GridSearchCV(clf, parameters)
grid_obj = grid_obj.fit(X_train, y_train)
# Set the clf to the best combination of parameters
clf = grid_obj.best_estimator_
tuned_params = clf.get_params()
# Train the model using the training sets
clf.fit(X_train, y_train)
# Prediction on test set
y_pred = clf.predict(X_test)
# Calculating the accuracy
acc_dt_tuned = metrics.accuracy_score(y_test, y_pred)
print('\nDecision Tree')
print('Default parameters:', default_params, 'Accuracy score:', acc_dt, sep='\n')
print('Tuned parameters:', tuned_params, 'Accuracy score:', acc_dt_tuned, sep='\n')

from sklearn.ensemble import RandomForestClassifier
# Create a Random Forest Classifier
rf = RandomForestClassifier()
default_params = rf.get_params()
# Train the model using the training sets
rf.fit(X_train,y_train)
# Prediction on test set
y_pred = rf.predict(X_test)
# Calculating the accuracy
acc_rf = metrics.accuracy_score(y_test, y_pred)
# Create a Random Forest Classifier
rf = RandomForestClassifier()
# Hyperparameter Optimization
parameters = {'n_estimators': [4, 6, 9, 10, 15],
'max_features': ['log2', 'sqrt','auto'],
'criterion': ['entropy', 'gini'],
'max_depth': [2, 3, 5, 10],
'min_samples_split': [2, 3, 5],
'min_samples_leaf': [1, 5, 8]
}
# Run the grid search
grid_obj = GridSearchCV(rf, parameters)
grid_obj = grid_obj.fit(X_train, y_train)
# Set the rf to the best combination of parameters
rf = grid_obj.best_estimator_
tuned_params = rf.get_params()
# Train the model using the training sets
rf.fit(X_train,y_train)
# Prediction on test set
y_pred = rf.predict(X_test)
# Calculating the accuracy
acc_rf_tuned = metrics.accuracy_score(y_test, y_pred)
print('\nRandom Forest')
print('Default parameters:', default_params, 'Accuracy score:', acc_rf, sep='\n')
print('Tuned parameters:', tuned_params, 'Accuracy score:', acc_rf_tuned, sep='\n')

# Creating scaled set to be used in model to improve the results
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
# Import Library of Support Vector Machine model
from sklearn import svm
# Create a Support Vector Classifier
svc = svm.SVC()
default_params = svc.get_params()
# Train the model using the training sets
svc.fit(X_train,y_train)
# Prediction on test data
y_pred = svc.predict(X_test)
# Calculating the accuracy
acc_svm = metrics.accuracy_score(y_test, y_pred)
# Create a Support Vector Classifier
svc = svm.SVC()
# Hyperparameter Optimization
parameters = [
{'C': [1, 10, 100, 1000], 'kernel': ['linear']},
{'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},
]
# Run the grid search
grid_obj = GridSearchCV(svc, parameters)
grid_obj = grid_obj.fit(X_train, y_train)
# Set the svc to the best combination of parameters
svc = grid_obj.best_estimator_
tuned_params = svc.get_params()
# Train the model using the training sets
svc.fit(X_train,y_train)
# Prediction on test data
y_pred = svc.predict(X_test)
# Calculating the accuracy
acc_svm_tuned = metrics.accuracy_score(y_test, y_pred)
print('\nSVM')
print('Default parameters:', default_params, 'Accuracy score:', acc_svm, sep='\n')
print('Tuned parameters:', tuned_params, 'Accuracy score:', acc_svm_tuned, sep='\n')

# Import library of KNeighborsClassifier model
from sklearn.neighbors import KNeighborsClassifier
# Create a KNN Classifier
knn = KNeighborsClassifier()
default_params = knn.get_params()
# Train the model using the training sets
knn.fit(X_train,y_train)
# Prediction on test data
y_pred = knn.predict(X_test)
# Calculating the accuracy
acc_knn = metrics.accuracy_score(y_test, y_pred)
# Create a KNN Classifier
knn = KNeighborsClassifier()
# Hyperparameter Optimization
parameters = {'n_neighbors': [3, 4, 5, 10],
'weights': ['uniform', 'distance'],
'algorithm' : ['auto', 'ball_tree', 'kd_tree', 'brute'],
'leaf_size' : [10, 20, 30, 50]
}
# Run the grid search
grid_obj = GridSearchCV(knn, parameters)
grid_obj = grid_obj.fit(X_train, y_train)
# Set the knn to the best combination of parameters
knn = grid_obj.best_estimator_
tuned_params = knn.get_params()
# Train the model using the training sets
knn.fit(X_train,y_train)
# Prediction on test data
y_pred = knn.predict(X_test)
# Calculating the accuracy
acc_knn_tuned = metrics.accuracy_score(y_test, y_pred)
print('\nKNN')
print('Default parameters:', default_params, 'Accuracy score:', acc_knn, sep='\n')
print('Tuned parameters:', tuned_params, 'Accuracy score:', acc_knn_tuned, sep='\n')
