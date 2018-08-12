import os
import pickle
from sklearn import svm
from sklearn import datasets
from resources.pickle.config import SKLEARN_PICKLE
clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target

clf.fit(X, y)
model_string = pickle.dumps(clf)

# Add code to save model to models directory
pickle_file = open(os.getcwd()+'/'+SKLEARN_PICKLE['output'], 'wb')
pickle_file.write(bytes(model_string))
pickle_file.close()