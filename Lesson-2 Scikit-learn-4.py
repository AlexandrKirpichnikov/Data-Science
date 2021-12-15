import pandas as pd
import numpy as np

df = pd.read_csv('creditcard.csv')

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

df['Class'].value_counts(normalize=True)

df.info()

pd.options.display.max_columns=100

df.head(10)

X = df.drop('Class', axis=1)

y = df['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100, stratify=y)

print('X_train ', X_train.shape)
print('X_test ', X_test.shape)
print('y_train ', y_train.shape)
print('y_test ', y_test.shape)

parameters = [{
    'n_estimators': [10, 15],
    'max_features': np.arange(3, 5),
    'max_depth': np.arange(4, 7)
}]

clf = GridSearchCV(
    estimator=RandomForestClassifier(random_state=100),
    param_grid=parameters,
    scoring='roc_auc',
    cv=3,
)

clf.fit(X_train, y_train)

clf.best_params_

clf = RandomForestClassifier(max_depth=6, max_features=3, n_estimators=15)

clf.fit(X_train, y_train)

y_pred = clf.predict_proba(X_test)

y_pred_proba = y_pred[:, 1]

from sklearn.metrics import roc_auc_score

roc_auc_score(y_test, y_pred_proba)

