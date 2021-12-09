from sklearn.ensemble import RandomForestRegressor

clf = RandomForestRegressor(n_estimators=1000, max_depth=12, random_state=42)

clf.fit(X_train, Y_train.values[:, 0])

y_pred_clf = clf.predict(X_test)
check_test_clf = pd.DataFrame({
    "Y_test": Y_test["price"],
    "Y_pred_clf": y_pred_clf.flatten()})

check_test_clf.head()

mean_squared_error_clf = mean_squared_error(check_test_clf["Y_pred_clf"], check_test_clf["Y_test"])
print(mean_squared_error_clf)

print(mean_squared_error_lr, mean_squared_error_clf