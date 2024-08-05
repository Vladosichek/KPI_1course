import pandas as pd
from sklearn.model_selection import train_test_split
import category_encoders as ce
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, label_binarize
from xgboost import XGBRFClassifier
from sklearn.metrics import confusion_matrix, roc_auc_score, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("car_evaluation.csv", header=None)
col_names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
df.columns = col_names
X = df.drop(['class'], axis=1)
Y = df['class']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=20)
encoder = ce.OrdinalEncoder(cols=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety'])
X_train = encoder.fit_transform(X_train)
X_test = encoder.transform(X_test)

rfc = RandomForestClassifier(random_state=10)
rfc.fit(X_train, y_train)
y_pred = rfc.predict(X_test)
label_encoder = LabelEncoder()
xgb = XGBRFClassifier(n_estimators=1000, random_state=1)
xgb.fit(X_train, label_encoder.fit_transform(y_train))
y_pred_xgb = label_encoder.inverse_transform(xgb.predict(X_test))

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title('Confusion Matrix - Random Forest')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.subplot(1, 2, 2)
sns.heatmap(confusion_matrix(y_test, y_pred_xgb), annot=True, fmt='d', cmap='Greens', cbar=False)
plt.title('Confusion Matrix - XGBoost')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.tight_layout()
plt.show()

class_labels = ['unacc', 'acc', 'good', 'vgood']
y_test_encoded = label_binarize(y_test, classes=class_labels)
y_pred_encoded = label_binarize(y_pred, classes=class_labels)
y_pred_boosted_encoded = label_binarize(y_pred_xgb, classes=class_labels)
roc_auc_scores = [roc_auc_score(y_test_encoded[:, i], y_pred_encoded[:, i]) for i in range(len(class_labels))]
roc_auc_scores_boosted = [roc_auc_score(y_test_encoded[:, i], y_pred_boosted_encoded[:, i]) for i in range(len(class_labels))]
print('\nROC AUC scores:\n', pd.DataFrame({'Random Forest':roc_auc_scores, 'XGBoost':roc_auc_scores_boosted}).set_index(pd.Index(class_labels)), sep='')
print('\n\nClassification report (Random Forest):\n', classification_report(y_test, y_pred))
print('\nClassification report (XGBoost):\n', classification_report(y_test, y_pred_xgb))
