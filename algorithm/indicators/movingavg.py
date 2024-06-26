from ..basicfunctions import add_column,delete_column,delete_row

def ma(data, lookback, close, position):

    data = add_column(data, 1)
    for i in range(len(data)):
        try:
            mean = (data[i - lookback + 1:i + 1,close].mean())

            data[i, position] = mean
            # print(data[i, position])
        except IndexError:
            pass
    data = delete_row(data, lookback)
    return data

def smoothed_ma(data, alpha, lookback, close, position):

    lookback = (2 * lookback) - 1
    alpha = alpha / (lookback + 1.0)
    beta  = 1 - alpha
    data = ma(data, lookback, close, position)
    data[lookback + 1, position] = (data[lookback + 1, close] * alpha)+(data[lookback, position] * beta)
    for i in range(lookback + 2, len(data)):
        try:
            data[i, position] = (data[i, close] * alpha) + (data[i - 1, position] * beta)
        except IndexError:
            pass
    return data

def rsi(data, lookback, close, position):
    data = add_column(data, 5)
    for i in range(len(data)):
        data[i, position] = data[i, close] - data[i - 1, close]
    for i in range(len(data)):
        if data[i, position] > 0:
            data[i, position + 1] = data[i, position]
        elif data[i, position] < 0:
            data[i, position + 2] = abs(data[i, position])
    data = smoothed_ma(data, 2, lookback, position + 1, position + 3)
    data = smoothed_ma(data, 2, lookback, position + 2, position + 4)
    data[:, position + 5] = data[:, position + 3] / data[:, position + 4]
    data[:, position + 6] = (100 - (100 / (1 + data[:, position + 5])))
    data = delete_column(data, position, 6)
    data = delete_row(data, lookback)
    return data