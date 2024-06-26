import numpy as np


def add_column(data, times):

    for i in range(1, times + 1):

        new = np.zeros((len(data), 1), dtype = float)

        data = np.append(data, new, axis = 1)

    return data

def delete_column(data, index, times):

    for i in range(1, times + 1):

        data = np.delete(data, index, axis = 1)

    return data

def add_row(data, times):

    for i in range(1, times + 1):

        columns = np.shape(data)[1]

        new = np.zeros((1, columns), dtype = float)

        data = np.append(data, new, axis = 0)

    return data

def rounding(data, how_far):

    data = data.round(decimals = how_far)

    return data

def performance(data,
                open_price,
                buy_column,
                sell_column,
                long_result_col,
                short_result_col,
                total_result_col):
    data = add_column(data,3)
    # Variable holding period
    for i in range(len(data)):

        try:

            if data[i, buy_column] == 1:

                for a in range(i + 1, i + 1000):

                    if data[a, buy_column] == 1 or data[a, sell_column] \
                            == -1:

                        data[a, long_result_col] = data[a, open_price] - \
                                                   data[i, open_price]

                        break

                    else:

                        continue

            else:

                continue

        except IndexError:

            pass

    for i in range(len(data)):

        try:

            if data[i, sell_column] == -1:

                for a in range(i + 1, i + 1000):

                    if data[a, buy_column] == 1 or data[a, sell_column] \
                            == -1:

                        data[a, short_result_col] = data[i, open_price] - \
                                                    data[a, open_price]

                        break

                    else:

                        continue

            else:
                continue

        except IndexError:

            pass

            # Aggregating the long & short results into one column
    data[:, total_result_col] = data[:, long_result_col] + \
                                data[:, short_result_col]

    # Profit factor
    total_net_profits = data[data[:, total_result_col] > 0, \
        total_result_col]
    total_net_losses  = data[data[:, total_result_col] < 0, \
        total_result_col]
    total_net_losses  = abs(total_net_losses)
    profit_factor     = round(np.sum(total_net_profits) / \
                              np.sum(total_net_losses), 2)

    # Hit ratio
    hit_ratio         = len(total_net_profits) / (len(total_net_losses) \
                                                  + len(total_net_profits))
    hit_ratio         = hit_ratio * 100

    # Risk-reward ratio
    average_gain            = total_net_profits.mean()
    average_loss            = total_net_losses.mean()
    realized_risk_reward    = average_gain / average_loss

    # Number of trades
    trades = len(total_net_losses) + len(total_net_profits)

    print('Hit Ratio         = ', hit_ratio)
    print('Profit factor     = ', profit_factor)
    print('Realized RR       = ', round(realized_risk_reward, 3))
    print('Number of trades  = ', trades)



def delete_row(data, number):

    data = data[number:, ]

    return data