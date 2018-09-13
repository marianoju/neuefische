import numpy as np
from sklearn.metrics import mean_squared_error, r2_score


def print_measurements(y_test, y_prediction):
    print("MSE:", mean_squared_error(y_test, y_prediction))
    print("RMSE:", np.sqrt(((y_test - y_prediction) ** 2).mean()))
    print("R²:", r2_score(y_test, y_prediction))
    print("RMSE % of mean:", np.sqrt(((y_test - y_prediction) ** 2).mean()) / y_test.mean())
    print("Calibration:", y_prediction.mean() / y_test.mean())
