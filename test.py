import numpy as np
import pandas as pd

from algorithm.indicators import marubozu_signal

def marubozu_test():
    arr = np.array([[23000, 23000, 23000,23010],
                    [23010, 23020, 23010,23020],
                    [23020, 23000, 23000,23030],
                    [23030, 23030, 23025,23025],
                    [23040, 23000, 23000,23050]])

    my_data = pd.DataFrame(marubozu_signal(arr))
    print(my_data.loc[my_data[4] == 1] )
    print(my_data.loc[my_data[5] == -1])
    print(my_data)

if __name__ == '__main__':
    marubozu_test()