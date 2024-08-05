import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import category_encoders as ce
from sklearn.preprocessing import RobustScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def prediction(classifier, X_train, y_train, X_test, y_test):
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    print('Model accuracy score: {0:0.4f}'.format(accuracy_score(y_test, y_pred)))
    y_pred_train = classifier.predict(X_train)
    print('Training-set accuracy score: {0:0.4f}'.format(accuracy_score(y_train, y_pred_train)))
    cm = confusion_matrix(y_test, y_pred)
    null_hpt=y_test.value_counts()
    null_accuracy = (max(null_hpt) / sum(null_hpt))
    print('Null accuracy score: {0:0.4f}'.format(null_accuracy))
    print(classification_report(y_test, y_pred))

    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.show()

#Prepearing
df = pd.read_csv("adult.csv", header=None, sep=',\s')
col_names = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation', 'relationship',
             'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income']
df.columns = col_names
categorical = [var for var in df.columns if df[var].dtype=='O']
df['workclass'].replace('?', np.NaN, inplace=True)
df['occupation'].replace('?', np.NaN, inplace=True)
df['native_country'].replace('?', np.NaN, inplace=True)
X = df.drop(['income'], axis=1)
y = df['income']

#Training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
for df2 in [X_train, X_test]:
    df2['workclass'].fillna(X_train['workclass'].mode()[0], inplace=True)
    df2['occupation'].fillna(X_train['occupation'].mode()[0], inplace=True)
    df2['native_country'].fillna(X_train['native_country'].mode()[0], inplace=True)
encoder = ce.OneHotEncoder(cols=['workclass', 'education', 'marital_status', 'occupation', 'relationship',
                                 'race', 'sex', 'native_country'])
X_train = encoder.fit_transform(X_train)
X_test = encoder.transform(X_test)
cols = X_train.columns
scaler = RobustScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
X_train = pd.DataFrame(X_train, columns=[cols])
X_test = pd.DataFrame(X_test, columns=[cols])

#Results
gnb = GaussianNB()
svc = SVC()
print("Gaussian Naive Bayes:")
prediction(gnb, X_train, y_train, X_test, y_test)
print("Support Vector Machine:")
prediction(svc, X_train, y_train, X_test, y_test)




