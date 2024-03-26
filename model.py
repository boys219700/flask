import numpy as np
from sklearn.linear_model import LinearRegression
def predict(marks):
    marks=np.array(marks)
    # Sample data
    X = np.array([[1], [2], [3], [4], [5]])  # Independent variable
    y = np.array([2, 3.1, 4.2, 5.3, 6.1])     # Dependent variable
    model = LinearRegression()
    model.fit(X, y)
    return model.predict(marks)

