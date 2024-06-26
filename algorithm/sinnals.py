from algorithm import add_column


def signal(data):
    """Open, High, Low, Close"""
    data = add_column(data, 2)

    for i in range(len(data)):

        try:

            # Bullish signal
            if data[i, 3] > data[i - 2, 3]:

                data[i + 1, 4] = 1

            # Bearish signal
            elif data[i, 3] < data[i - 2, 3]:

                data[i + 1, 5] = -1

        except IndexError:

            pass

    return data