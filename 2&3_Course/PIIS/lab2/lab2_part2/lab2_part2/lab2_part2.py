import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

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

    pca = PCA(n_components=2)
    pca.fit(X_train)
    X_test_pca = pca.transform(X_test)
    plt.scatter(X_test_pca[:, 0], y=X_test_pca[:, 1], c=y_pred)
    plt.show()

df = pd.read_csv('teleCust1000t.csv')
X = df[['region', 'tenure', 'age', 'marital', 'address', 'income', 'ed', 'employ', 'retire', 'gender', 'reside']]
y = df['custcat']
standardizer=StandardScaler()
X = standardizer.fit(X).transform(X.astype(float))
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=4)
for j in ['minkowski', 'euclidean', 'manhattan']:
       knn=KNeighborsClassifier(n_neighbors=8, metric=j, n_jobs=-1)
       print(j)
       prediction(knn, X_train,y_train,X_test,y_test)