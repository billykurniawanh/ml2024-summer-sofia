import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    N = int(input("Enter a positive number N: "))

    X = []
    Y = []
    for i in range(N):
        x = int(input("Enter x value: "))
        y = int(input("Enter y value: "))
        X.append(x)
        Y.append(y)

    precision = precision_score(X, Y)
    recall = recall_score(X, Y)

    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

main()