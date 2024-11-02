from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
from sklearn.metrics import confusion_matrix, accuracy_score
wine = load_wine()
X = wine.data
y = wine.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_test_pred = gnb.predict(X_test)
y_pred = gnb.predict([[13.0, 2.0, 2.5, 15.0, 95.0, 2.0, 2.5, 0.3, 2.0, 5.0, 1.0, 3.0, 1.2]])
pred_species = [wine.target_names[p] for p in y_pred]
print("Predictions:", pred_species)
cm = confusion_matrix(y_test, y_test_pred)
print("Confusion Matrix:\n", cm)
ac = accuracy_score(y_test, y_test_pred)
print("Accuracy:",ac)