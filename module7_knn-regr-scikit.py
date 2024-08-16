import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

def main():
    N = int(input("Enter a positive number N: "))
    k = int(input("Enter a positive number k: "))

    if k > N:
        print("Error")
        return

    X = []
    Y = []
    for _ in range(N):
        x = float(input("Enter x value: "))
        y = float(input("Enter y value: "))
        X.append([x])
        Y.append(y)

    X = np.array(X)
    Y = np.array(Y)

    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X, Y)

    Output_X = float(input("Enter the input X: "))
    Output_Y = model.predict(np.array([[Output_X]]))
    print(f"Your point is ({Output_X}, {Output_Y})")

    variance = np.var(Y)
    print(f"Variance: {variance}")

main()