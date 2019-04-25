import numpy as np
import scipy.optimize


def main():
    # max z = 2x1 + 3x2
    # const:
    # x1 + 2x2 < 6
    # 2x1 + x2 < 8
    c = [-2, -3]
    A = [[1, 2], [2, 1]]
    b = [6, 8]
    x0_bounds = (0, None)
    x1_bounds = (0, None)
    bounds = (x0_bounds, x1_bounds)

    res = scipy.optimize.linprog(c, A, b, bounds=bounds, method='simplex', options={"disp": True})
    print(res)
    pass


if __name__ == "__main__":
    main()
