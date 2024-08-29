import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():
    N = int(input("Enter a positive number N: "))

    X_train = []
    Y_train = []
    for i in range(N):
        x = float(input("Enter x value for training data: "))
        y = int(input("Enter y value for training data: "))
        X_train.append(x)
        Y_train.append(y)


    M = int(input("Enter a positive number M: "))

    X_test = []
    Y_test = []
    for i in range(M):
        x = float(input("Enter x value for test data: "))
        y = int(input("Enter y value for test data: "))
        X_test.append(x)
        Y_test.append(y)

    X_train = np.array(X_train).reshape(-1, 1)
    Y_train = np.array(Y_train)
    X_test = np.array(X_test).reshape(-1, 1)
    Y_test = np.array(Y_test)

    max_k = 0
    max_accuracy = 0.0

    for k in range(1, N+1):
        classifier = KNeighborsClassifier(n_neighbors=k)
        classifier.fit(X_train, Y_train)
        Y_prediction = classifier.predict(X_test)
        accuracy = accuracy_score(Y_test, Y_prediction)
        if accuracy > max_accuracy:
            max_accuracy = accuracy
            max_k = k

    print(f"Best k value: {max_k}")
    print(f"Best accuracy: {max_accuracy}")

main()