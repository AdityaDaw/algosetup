from ..basicfunctions import add_column

def quintuplets_signals(data, open_column =0, close_column = 3, buy_column =4, sell_column =5,low_column=2,high_column=1, body = 10):
    """

    If the latest five close prices are each greater than their open prices, as well as the close prices preceding them, and each candlestick respects a maximum body size, then print 1 in the next buy row.
    If the latest five close prices are each lower than their open prices, as well as the close prices preceding them, and each candlestick respects a maximum body size, then print −1 in the next sell row.

    :param data:
    :param open_column:
    :param close_column:
    :param buy_column:
    :param sell_column:
    :param low_column:
    :param high_column:
    :param body:
    :return:
    """
    data = add_column(data, 2)

    for i in range(len(data)):

        try:

            # Bullish pattern
            if data[i, close_column]>data[i, open_column] and \
                    data[i, close_column]>data[i - 1, close_column] and \
                    data[i, close_column]-data[i, open_column]<body and \
                    data[i-1, close_column]>data[i-1, open_column] and \
                    data[i-1, close_column]>data[i-2, close_column] and \
                    data[i-1, close_column]-data[i-1, open_column]<body and \
                    data[i-2, close_column]>data[i-2, open_column] and \
                    data[i-2, close_column]>data[i-3, close_column] and \
                    data[i-2, close_column]-data[i-2, open_column]<body and \
                    data[i-3, close_column]>data[i-3, open_column] and \
                    data[i-3, close_column]>data[i-4, close_column] and \
                    data[i-3, close_column]-data[i-3, open_column]<body and \
                    data[i-4, close_column]>data[i-4, open_column] and \
                    data[i-4, close_column]-data[i-4, open_column]<body and \
                    data[i, buy_column] == 0:

                data[i + 1, buy_column] = 1

                # Bearish pattern
            elif  data[i, close_column]<data[i, open_column] and \
                    data[i, close_column]<data[i-1, close_column] and \
                    data[i, open_column]-data[i, close_column]<body and \
                    data[i-1, close_column]<data[i-1, open_column] and \
                    data[i-1, close_column]<data[i-2, close_column] and \
                    data[i-1, open_column]-data[i-1, close_column]<body and \
                    data[i-2, close_column]<data[i-2, open_column] and \
                    data[i-2, close_column]<data[i-3, close_column] and \
                    data[i-2, open_column]-data[i-2, close_column]<body and \
                    data[i-3, close_column]<data[i-3, open_column] and \
                    data[i-3, close_column]<data[i-4, close_column] and \
                    data[i-3, open_column]-data[i-3, close_column]<body and \
                    data[i-4, close_column]<data[i-4, open_column] and \
                    data[i-4, open_column]-data[i-4, close_column]<body and \
                    data[i, sell_column] == 0:

                data[i + 1, sell_column] = -1

        except IndexError:

            pass

    return data


def bottle_signal(data, open_column =0, close_column = 3, buy_column =4, sell_column =5,low_column=2,high_column=1, body = 10):
    """
    The bullish Bottle pattern is composed of a bullish candle followed by another bullish candle with no wick on the low side but with a wick on the high side. At the same time, the second candle must open below the last candle’s close, which is considered a gap lower (or inside gap).

    The bearish Bottle pattern is composed of a bearish candlestick followed by another bearish candlestick with no wick on the high side but with a wick on the low side. At the same time, the second candlestick must open above the last candlestick’s close, which is considered a gap higher. Figure 5-12 illustrates the bearish Bottle.

    :param data:
    :param open_column:
    :param close_column:
    :param buy_column:
    :param sell_column:
    :param low_column:
    :param high_column:
    :param body:
    :return:
    """
    data = add_column(data, 2)

    for i in range(len(data)):

        try:

            # Bullish pattern
            if data[i, close_column] > data[i, open_column] and \
                    data[i, open_column] == data[i, low_column] and \
                    data[i - 1, close_column] > data[i - 1, open_column] and \
                    data[i, open_column] < data[i - 1, close_column] and \
                    data[i, buy_column] == 0:

                data[i + 1, buy_column] = 1

                # Bearish pattern
            elif data[i, close_column] < data[i, open_column] and \
                    data[i, open_column] == data[i, high_column] and \
                    data[i - 1, close_column] < data[i - 1, open_column] and \
                    data[i, open_column] > data[i - 1, close_column] and \
                    data[i, sell_column] == 0:

                data[i + 1, sell_column] = -1

        except IndexError:

            pass

    return data


def slingshot_signal(data, open_column =0, close_column = 3, buy_column =4, sell_column =5,low_column=2,high_column=1):
    """
    First, the pattern is characterized by having a first bullish candle followed by a higher one confirming a bullish bias, and then it has two more candlesticks, with the latter one not surpassing the high of the former. Finally, the last candlestick must have a low at or below the high of the first candlestick and a close higher than the high of the second candlestick. There is no strict rule about the color of the second and third candles. Figure 5-15 shows the perfect bullish Slingshot pattern.

    The bearish Slingshot pattern (Figure 5-16) is characterized by having a first bearish candlestick followed by a lower one confirming a bearish bias, and then it has two more candlesticks, with the latter one not breaking the low of the former. Finally, the last candlestick must have a high at or above the low of the first candlestick and a close lower than the low of the second candlestick.

    :param data:
    :param open_column:
    :param close_column:
    :param buy_column:
    :param sell_column:
    :param low_column:
    :param high_column:
    :return:
    """
    data = add_column(data, 2)

    for i in range(len(data)):

        try:

            # Bullish pattern
            if data[i, close_column] > data[i - 1, high_column] and \
                    data[i, close_column] > data[i - 2, high_column] and \
                    data[i, low_column] <= data[i - 3, high_column] and \
                    data[i, close_column] > data[i, open_column] and \
                    data[i - 1, close_column] >= data[i - 3, high_column] and \
                    data[i - 2, low_column] >= data[i - 3, low_column] and \
                    data[i - 2, close_column] > data[i - 2, open_column] and \
                    data[i - 2, close_column] > data[i - 3, high_column] and \
                    data[i - 1, high_column] <= data[i - 2, high_column]:

                data[i + 1, buy_column] = 1

                # Bearish pattern
            elif data[i, close_column] < data[i - 1, low_column] and \
                    data[i, close_column] < data[i - 2, low_column] and \
                    data[i, high_column] >= data[i - 3, low_column] and \
                    data[i, close_column] < data[i, open_column] and \
                    data[i - 1, high_column] <= data[i - 3, high_column] and \
                    data[i - 2, close_column] <= data[i - 3, low_column] and \
                    data[i - 2, close_column] < data[i - 2, open_column] and \
                    data[i - 2, close_column] < data[i - 3, low_column] and \
                    data[i - 1, low_column] >= data[i - 2, low_column]:

                data[i + 1, sell_column] = -1

        except IndexError:

            pass

    return data


def h_pattern_signal(data, open_column =0, close_column = 3, buy_column =4, sell_column =5,low_column=2,high_column=1):
    """
    The H pattern is a three-candle continuation configuration. The bullish H pattern (Figure 5-19) is composed of a bullish candle followed by an indecision candlestick3 that has its open price equal to its close price. Next, the third candle must be bullish, and its close price must be higher than the indecision candle’s close. Finally, the low of the third candle must be higher than the low of the indecision candle.

    The bearish H pattern (Figure 5-20) is composed of a bearish candle followed by an indecision candle; next, the third candle must be bearish, and its close must be lower than the indecision candle’s close. Finally, the high of the third candle must be lower than the high of the indecision candle.

    :param data:
    :param open_column:
    :param close_column:
    :param buy_column:
    :param sell_column:
    :param low_column:
    :param high_column:
    :return:
    """
    data = add_column(data, 2)

    for i in range(len(data)):

        try:

            # Bullish pattern
            if data[i, close_column] > data[i, open_column] and \
                    data[i, close_column] > data[i - 1, close_column] and \
                    data[i, low_column] > data[i - 1, low_column] and \
                    data[i - 1, close_column] == data[i - 1, open_column] and \
                    data[i - 2, close_column] > data[i - 2, open_column] and \
                    data[i - 2, high_column] < data[i - 1, high_column]:

                data[i + 1, buy_column] = 1

                # Bearish pattern
            elif data[i, close_column] < data[i, open_column] and \
                    data[i, close_column] < data[i - 1, close_column] and \
                    data[i, low_column] < data[i - 1, low_column] and \
                    data[i - 1, close_column] == data[i - 1, open_column] and \
                    data[i - 2, close_column] < data[i - 2, open_column] and \
                    data[i - 2, low_column] > data[i - 1, low_column]:

                data[i + 1, sell_column] = -1

        except IndexError:

            pass

    return data


def doji_signal(data, open_column =0, close_column = 3, buy_column =4, sell_column =5,low_column=2,high_column=1):
    """

    If the current close price is greater than the current open price, the previous close price equals the open price, and the prior close price is lower than the prior open price, then print 1 in the next row.
    If the current close price is lower than the current open price, the previous close price equals the open price, and the prior close price is greater than the prior open price, then print −1 in the next row.

    :param data:
    :param open_column:
    :param close_column:
    :param buy_column:
    :param sell_column:
    :param low_column:
    :param high_column:
    :return:
    """
    data = add_column(data, 2)

    for i in range(len(data)):

        try:

            # Bullish pattern
            if data[i, close_column] > data[i, open_column] and \
                    data[i, close_column] > data[i - 1, close_column] and \
                    data[i - 1, close_column] == data[i - 1, open_column] and \
                    data[i - 2, close_column] < data[i - 2, open_column] and \
                    data[i - 2, close_column] < data[i - 2, open_column]:

                data[i + 1, buy_column] = 1

                # Bearish pattern
            elif data[i, close_column] < data[i, open_column] and \
                    data[i, close_column] < data[i - 1, close_column] and \
                    data[i - 1, close_column] == data[i - 1, open_column] and \
                    data[i - 2, close_column] > data[i - 2, open_column] and \
                    data[i - 2, close_column] > data[i - 2, open_column]:

                data[i + 1, sell_column] = -1

        except IndexError:

            pass

    return data


def harami_signal(data, open_column =0, close_column = 3, buy_column =4, sell_column =5,low_column=2,high_column=1):
    """

    If the current close price is greater than the current open price and the previous close price, and the current open price is greater than the previous close price but lower than the previous open price, then print 1 in the next buy row.
    If the current close price is lower than the current open price and the previous close price, and the current open price is lower than the previous close price but greater than the previous open price, then print −1 in the next sell row.

    :param data:
    :param open_column:
    :param close_column:
    :param buy_column:
    :param sell_column:
    :param low_column:
    :param high_column:
    :return:
    """
    data = add_column(data, 2)

    for i in range(len(data)):

        try:

            # Bullish pattern
            if data[i, close_column] < data[i - 1, open_column] and \
                    data[i, open_column] > data[i - 1, close_column] and \
                    data[i, high_column] < data[i - 1, high_column] and \
                    data[i, low_column] > data[i - 1, low_column] and \
                    data[i, close_column] > data[i, open_column] and \
                    data[i - 1, close_column] < data[i - 1, open_column] and \
                    data[i - 2, close_column] < data[i - 2, open_column]:

                data[i + 1, buy_column] = 1

                # Bearish pattern
            elif data[i, close_column] > data[i - 1, open_column] and \
                    data[i, open_column] < data[i - 1, close_column] and \
                    data[i, high_column] < data[i - 1, high_column] and \
                    data[i, low_column] > data[i - 1, low_column] and \
                    data[i, close_column] < data[i, open_column] and \
                    data[i - 1, close_column] > data[i - 1, open_column] and \
                    data[i - 2, close_column] > data[i - 2, open_column]:

                data[i + 1, sell_column] = -1

        except IndexError:

            pass

    return data


def strict_harami_signal(data, open_column =0, close_column = 3, buy_column =4, sell_column =5,low_column=2,high_column=1):
    """

    If the current candlestick is bullish and fully englobed within the previous bearish one, then print 1 in the next buy row.
    If the current candlestick is bearish and fully englobed within the previous bullish one, then print −1 in the next sell row.

    :param data:
    :param open_column:
    :param close_column:
    :param buy_column:
    :param sell_column:
    :param low_column:
    :param high_column:
    :return:
    """

    data = add_column(data, 2)

    for i in range(len(data)):

        try:

            # Bullish pattern
            if data[i, close_column] > data[i, open_column] and \
                    data[i, high_column] < data[i - 1, open_column] and \
                    data[i, low_column] > data[i - 1, close_column] and \
                    data[i - 1, close_column] < data[i - 1, open_column] and \
                    data[i - 2, close_column] < data[i - 2, open_column]:


                data[i + 1, buy_column] = 1

                # Bearish pattern
            elif data[i, close_column] < data[i, open_column] and \
                    data[i, high_column] < data[i - 1, close_column] and \
                    data[i, low_column] > data[i - 1, open_column] and \
                    data[i - 1, close_column] > data[i - 1, open_column] and \
                    data[i - 2, close_column] > data[i - 2, open_column]:

                data[i + 1, sell_column] = -1

        except IndexError:

            pass

    return data


def on_neck_signal(data, open_column =0, close_column = 3, buy_column =4, sell_column =5,low_column=2,high_column=1):
    """

    If the current close price is greater than the current open price and is equal to the previous close price, and the current open price is lower than the previous close price, then print 1 in the next buy row.
    If the current close price is lower than the current open price and is equal to the previous close price, and the current open price is greater than the previous close price, then print −1 in the next sell row.

    :param data:
    :param open_column:
    :param close_column:
    :param buy_column:
    :param sell_column:
    :param low_column:
    :param high_column:
    :return:
    """
    data = add_column(data, 2)

    for i in range(len(data)):

        try:

            # Bullish pattern
            if data[i, close_column] > data[i, open_column] and \
                    data[i, close_column] == data[i - 1, close_column] and \
                    data[i, open_column] < data[i - 1, close_column] and \
                    data[i - 1, close_column] < data[i - 1, open_column]:

                data[i + 1, buy_column] = 1

                # Bearish pattern
            elif data[i, close_column] < data[i, open_column] and \
                    data[i, close_column] == data[i - 1, close_column] and \
                    data[i, open_column] > data[i - 1, close_column] and \
                    data[i - 1, close_column] > data[i - 1, open_column]:

                data[i + 1, sell_column] = -1

        except IndexError:

            pass

    return data


# def on_neck_signal(data, open_column =0, close_column = 3, buy_column =4, sell_column =5,low_column=2,high_column=1):

    