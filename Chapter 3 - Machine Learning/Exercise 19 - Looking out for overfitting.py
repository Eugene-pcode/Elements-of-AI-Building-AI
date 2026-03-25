from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import numpy as np

# do not edit this
# create fake data
x, y = make_moons(
    n_samples=500,  # the number of observations
    random_state=42,
    noise=0.3
)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

# Create a classifier and fit it to our data
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)

y_predict = np.empty(len(y_test), dtype=np.int64)

lines = []

def dist(a, b):
    return np.sqrt(np.sum((a - b)**2))

def main(X_train, X_test, y_train, y_test):
    global y_predict
    k = 3

    for i, test_item in enumerate(X_test):
        distances = [dist(train_item, test_item) for train_item in X_train]
        nearest_indices = np.argsort(distances)[:k]
        nearest_labels = y_train[nearest_indices]
        
        # Majority vote (not average)
        unique, counts = np.unique(nearest_labels, return_counts=True)
        y_predict[i] = unique[np.argmax(counts)]
    
    return y_predict

# Run custom KNN
y_pred_custom = main(x_train, x_test, y_train, y_test)

# Get scikit-learn predictions
y_pred_sklearn = knn.predict(x_test)

# Calculate accuracies
custom_accuracy = np.mean(y_pred_custom == y_test)
sklearn_accuracy = np.mean(y_pred_sklearn == y_test)

print("Custom KNN predictions:", y_pred_custom[:10])
print("Scikit-learn predictions:", y_pred_sklearn[:10])
print("Actual labels:           ", y_test[:10])
print()
print("Custom KNN accuracy:     %f" % custom_accuracy)
print("Scikit-learn accuracy:   %f" % sklearn_accuracy)