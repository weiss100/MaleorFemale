import csv
import os

from sklearn import tree
from sklearn import svm
from sklearn import neighbors
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# data/body_measurements.csv: 340 real measurements (see data/README.md)
# columns: height_cm, weight_kg, shoe_size_eu, gender
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "body_measurements.csv")
with open(path, newline="") as f:
    rows = list(csv.DictReader(f))

#[height, weight, shoe_size]
X = [[int(r["height_cm"]), int(r["weight_kg"]), int(r["shoe_size_eu"])] for r in rows]
Y = [r["gender"] for r in rows]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.3, stratify=Y, random_state=0)

# SVM and KNN depend on feature scales (cm vs. kg vs. shoe size), so they get a scaler
classifiers = {
    "Decision Tree": tree.DecisionTreeClassifier(random_state=0),
    "SVM": make_pipeline(StandardScaler(), svm.SVC()),
    "Naive Bayes": GaussianNB(),
    "K neighbors": make_pipeline(StandardScaler(), neighbors.KNeighborsClassifier()),
}

# test accuracy on the held-out split, plus 5-fold cross-validation on all data
# (a single split of 102 test samples is still noisy)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
test_acc, cv_acc = {}, {}
for name, clf in classifiers.items():
    clf.fit(X_train, Y_train)
    test_acc[name] = accuracy_score(Y_test, clf.predict(X_test))
    scores = cross_val_score(clf, X, Y, cv=cv)
    cv_acc[name] = scores.mean()
    print("%-14s test accuracy: %.3f | 5-fold CV: %.3f (+/- %.3f)"
          % (name, test_acc[name], cv_acc[name], scores.std()))

# the best classifier is picked by cross-validation, not by the single split
best_accuracy = max(cv_acc.values())
best = [name for name, acc in cv_acc.items() if acc == best_accuracy]
print("Best classifier (CV): %s (%.3f)" % (", ".join(best), best_accuracy))
