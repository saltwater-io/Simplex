import numpy as np
import scipy.optimize


def main():
    # Problems 2
    # max z = 2x1 + 3x2
    # const:
    # x1 + 2x2 < 6
    # 2x1 + x2 < 8
    # coefficients set to negative for minimum
    # z = -1(function value)

    c = [-2, -3]
    A = [[1, 2], [2, 1]]
    b = [6, 8]
    x0_bounds = (0, None)
    x1_bounds = (0, None)
    bounds = (x0_bounds, x1_bounds)

    res = scipy.optimize.linprog(c, A, b, bounds=bounds, method='simplex', options={"disp": True})
    print(" ")
    print("4.6 Problem 2: ")
    print(res)

    print(" ")

    # Problem 3
    # max z = 2x1 -x2 + x3
    # const:
    #  3x1 + x2 + x3 < 60
    # 2x1 + x2 + 2x3 < 20
    # 2x1 + 2x2 + x3 < 20
    # x1,x2,x3 > 0

    c = [-2, 1, -1]  # reverse sign on coefficients
    A = [[3, 1, 1], [2, 1, 2], [2, 2, 1]]
    b = [60, 20, 20]
    x0_bounds = (0, None)
    x1_bounds = (0, None)
    x2_bounds = (0,None)
    bounds = (x0_bounds, x1_bounds, x2_bounds)
    print("4.6 Problem 3: ")
    res = scipy.optimize.linprog(c, A, b, bounds=bounds, method='simplex', options={"disp": True})
    print(res)

    pass


if __name__ == "__main__":
    main()

