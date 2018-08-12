import os
import pickle
from sklearn import svm
from sklearn import datasets
from sklearn.externals import joblib
from resources.pickle.config import JOBLIB_PICKLE
clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target

clf.fit(X, y)
model_string = pickle.dumps(clf)

# Add code to save model to models directory
joblib.dump(clf, os.getcwd()+'/'+JOBLIB_PICKLE['output'])