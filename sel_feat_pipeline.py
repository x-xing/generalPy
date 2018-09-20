from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import SelectFromModel

# Load dataset
iris = datasets.load_iris()
X, y = iris.data, iris.target

rf_feature_imp = RandomForestClassifier(100)
feat_selection = SelectFromModel(rf_feature_imp, threshold=0.01)

clf = RandomForestClassifier(5000)

model = Pipeline([
          ('fs', feat_selection), 
          ('clf', clf), 
        ])

params = {
    'fs__threshold': [0.01, 0.05, 0.1	],
    'fs__estimator__max_features': ['auto', 'sqrt', 'log2'],
    'clf__max_features': ['auto', 'sqrt', 'log2'],
}

gs = GridSearchCV(model, params)
gs.fit(X,y)

fs = gs.best_estimator_.named_steps['fs']

#Create an example list from the feature_names:
feature_names_example = [iris.feature_names]
#Use the feature selector to transform this example.
selected_features = fs.transform(feature_names_example)

print selected_features[0] # Select the one example
# ['sepal length (cm)' 'petal length (cm)' 'petal width (cm)']