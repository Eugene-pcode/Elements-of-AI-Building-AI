import numpy as np
from io import StringIO

train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''

def main():
    np.set_printoptions(precision=1)

    # Use StringIO to treat strings as file-like objects
    data_train = np.genfromtxt(StringIO(train_string), skip_header=1)
    data_test = np.genfromtxt(StringIO(test_string), skip_header=1)

    # Extract features (all columns except last)
    x_train = data_train[:, :-1]
    y_train = data_train[:, -1]

    # Extract test features
    x_test = data_test[:, :-1]

    # Solve least squares to find coefficients
    coeff = np.linalg.lstsq(x_train, y_train, rcond=None)[0]

    # Print coefficients and test predictions
    print(coeff)
    print(x_test @ coeff)

main()