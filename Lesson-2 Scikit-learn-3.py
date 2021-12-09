print(clf.feature_importances_)

feature_importance = pd.DataFrame({'name':X.columns,
                                   'feature_importance':clf.feature_importances_},
                                  columns=['feature_importance', 'name'])
feature_importance

feature_importance.nlargest(2, 'feature_importance')