import matplotlib.pyplot as plt
import numpy as np

def ohlc_plot_candles(data, window):
    sample = data[-window:, ]
    sample = data
    for i in range(len(sample)):
        plt.vlines(x = i, ymin = sample[i, 2], ymax = sample[i, 1],
                   color = 'black', linewidth = 1)
        if sample[i, 3] > sample[i, 0]:
            plt.vlines(x = i, ymin = sample[i, 0], ymax = sample[i, 3],
                       color = 'green', linewidth = 3)
        if sample[i, 3] < sample[i, 0]:
            plt.vlines(x = i, ymin = sample[i, 3], ymax = sample[i, 0],
                       color = 'red', linewidth = 3)
        if sample[i, 3] == sample[i, 0]:
            plt.vlines(x = i, ymin = sample[i, 3], ymax = sample[i, 0] +
                                                          0.00003, color = 'black', linewidth = 1.00)
    plt.grid()
    # plt.show(block=True)

def ohlc_plot_candles_main(data,):
    ohlc_plot_candles(data, len(data))
    plt.show(block=True)

def signal_chart(data, position, buy_column, sell_column, window = 500):

    # sample = np.divide(data[-window:, ],np.mean(data[-window:, ]))
    sample = data[-window:, ]

    fig, ax = plt.subplots(figsize = (10, 5))
    ohlc_plot_candles(data, window)

    for i in range(len(sample)):
        if sample[i, buy_column] != 0:
            x = i
            y = sample[i, position]
            # print(f"We are annoting {x},{y}")
            ax.annotate(' ', xy = (x, y),
                        arrowprops = dict(width = 9, headlength = 11,
                                          headwidth = 11, facecolor = 'green', color =
                                          'green'))

        elif sample[i, sell_column] != 0:
            x = i
            y = sample[i, position]
            # print(f"We are annoting sell - {x},{y}")
            ax.annotate(' ', xy = (x, y),
                        arrowprops = dict(width = 9, headlength = -11,
                                          headwidth = -11, facecolor = 'red', color =
                                          'red'))

    plt.show(block=True)
