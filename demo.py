from sklearn import tree
from sklearn import svm
from sklearn import neighbors
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

#[height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],[177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']

#test data
X_test=[[198,92,48],[184,84,44],[183,83,44],[166,47,36],[170,60,38],[172,64,39],[182,80,42],[180,80,43]]
Y_test=['male','male','male','female','female','female','male','male']

classifiers = {
    "Decision Tree": tree.DecisionTreeClassifier(random_state=0),
    "SVM": svm.SVC(),
    "Naive Bayes": GaussianNB(),
    "K neighbors": neighbors.KNeighborsClassifier(),
}

# train every classifier and measure its accuracy on the test data
accuracies = {}
for name, clf in classifiers.items():
    clf.fit(X, Y)
    prediction = clf.predict(X_test)
    accuracies[name] = accuracy_score(Y_test, prediction)
    print("Prediction for %s : %s" % (name, prediction))
    print("Accuracy for %s : %s" % (name, accuracies[name]))

# compare the results and print the best one(s); ties are reported, not hidden
best_accuracy = max(accuracies.values())
best = [name for name, acc in accuracies.items() if acc == best_accuracy]
print("Best classifier: %s (accuracy %s)" % (", ".join(best), best_accuracy))
