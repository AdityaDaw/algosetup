from ..basicfunctions import add_column

def marubozu_signal(data, open_column = 0, high_column =1, low_column =2, close_column =3,
           buy_column =4, sell_column =5):
    """
    Algorithmically, the conditions need to be as follows:
    If the close price is greater than the open price, the high price equals the close price, and the low price equals the open price, then print 1 in the next row of the column reserved for buy signals.

    If the close price is lower than the open price, the high price equals the open price, and the low price equals the close price, then print −1 in the next row of the column reserved for sell signals.
    :param data:
    :param open_column:
    :param high_column:
    :param low_column:
    :param close_column:
    :param buy_column:
    :param sell_column:
    :return:
    """

    data = add_column(data, 2)

    for i in range(len(data)):
        try:
            # Bullish pattern
            if data[i, close_column] > data[i, open_column] and \
                    data[i, high_column] == data[i, close_column] and \
                    data[i, low_column] == data[i, open_column] and \
                    data[i, buy_column] == 0:
                data[i + 1, buy_column] = 1

            # Bearish pattern
            elif data[i, close_column] < data[i, open_column] and \
                    data[i, high_column] == data[i, open_column] and \
                    data[i, low_column] == data[i, close_column] and \
                    data[i, sell_column] == 0:

                data[i + 1, sell_column] = -1

        except IndexError:
            pass

    return data


def three_column_signal(data, open_column =0, close_column = 3, buy_column =4, sell_column =5,body = 10):
    data = add_column(data, 2)
    for i in range(len(data)):
        try:
            # Bullish pattern
            if data[i, close_column] - data[i, open_column] > body and \
                    data[i - 1, close_column] - data[i - 1, open_column] > body \
                    and data[i - 2, close_column] - data[i - 2, open_column] > body \
                    and data[i, close_column] > data[i - 1, close_column] \
                    and data[i - 1, close_column] > data[i - 2, close_column] \
                    and data[i - 2, close_column] > data[i - 3, close_column] \
                    and data[i, buy_column] == 0:

                data[i + 1, buy_column] = 1

            # Bearish pattern
            elif data[i, close_column] - data[i, open_column] > body and \
                    data[i - 1, close_column] - data[i - 1, open_column] > \
                    body and data[i - 2, close_column] - \
                    data[i - 2, open_column] > body and data[i, close_column] \
                    < data[i - 1, close_column] and data[i - 1, close_column] \
                    < data[i - 2, close_column] and data[i - 2, close_column] \
                    < data[i - 3, close_column] and data[i, sell_column] == 0:
                data[i + 1, sell_column] = -1
        except IndexError:
            pass
    return data


def tasuki_signal(data, open_column =0, close_column = 3, buy_column =4, sell_column =5):
    """
    Algorithmically, the conditions need to be as follows:

    If the close price from two periods ago is greater than the open price from two periods ago, the open price from one period ago is greater than the close two periods ago, the close price from one period ago is greater than the open price from one period ago, and the current close price is greater than the close price two periods ago, print 1 in the next row of the column reserved for buy signals.
    If the close price from two periods ago is lower than the open price from two periods ago, the open price from one period ago is lower than the close two periods ago, the close price from one period ago is lower than the open price from one period ago, and the current close price is lower than the close price two periods ago, then print −1 in the next row of the column reserved for sell signals.

    :param data:
    :param open_column:
    :param close_column:
    :param buy_column:
    :param sell_column:
    :return:
    """
    data = add_column(data, 2)
    for i in range(len(data)):
        try:
            # Bullish pattern
            if data[i, close_column] < data[i, open_column] and \
                    data[i, close_column] < data[i - 1, open_column] and \
                    data[i, close_column] > data[i - 2, close_column] and \
                    data[i - 1, close_column] > data[i - 1, open_column] and \
                    data[i - 1, open_column] > data[i - 2, close_column] and \
                    data[i - 2, close_column] > data[i - 2, open_column]:
                data[i + 1, buy_column] = 1
            # Bearish pattern
            elif data[i, close_column] > data[i, open_column] and \
                    data[i, close_column] > data[i - 1, open_column] and \
                    data[i, close_column] < data[i - 2, close_column] and \
                    data[i - 1, close_column] < data[i - 1, open_column] and \
                    data[i - 1, open_column] < data[i - 2, close_column] and \
                    data[i - 2, close_column] < data[i - 2, open_column]:
                data[i + 1, sell_column] = -1
        except IndexError:
            pass
    return data