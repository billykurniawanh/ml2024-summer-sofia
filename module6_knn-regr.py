import numpy as np

class Model:
    def __init__(self, k):
        self.k = k
        self.X = None
        self.Y = None

    def add_points(self, X, Y):
        self.X = np.array(X)
        self.Y = np.array(Y)

    def predict(self, X):
        distances = np.sqrt(np.sum((self.X - np.array(X)) ** 2, axis=1))
        nearest = np.argsort(distances)[:self.k]
        return np.mean(self.Y[nearest])

def main():
    N = int(input("Enter a positive number N: "))
    k = int(input("Enter a positive number k: "))
    
    if k > N:
        print("Error")
        return

    model = Model(k)

    X = []
    Y = []
    for _ in range(N):
        x = float(input("Enter x value: "))
        y = float(input("Enter y value: "))
        X.append([x])
        Y.append(y)
    model.add_points(X, Y)

    Output_X = float(input("Enter the input X: "))
    Output_Y = model.predict([Output_X])
    print(f"Your point is ({Output_X}, {Output_Y})")

main()