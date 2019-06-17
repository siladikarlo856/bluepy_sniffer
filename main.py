#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from ble_sniffer import *

def main():
    style.use('fivethirtyeight')

    print("TENG BLE sniffer")

    # start BLE scanner in background
    BleSnifferThread()

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)

    def myAnimateFunc(i):
        graphData = open('myData.txt', 'r').read();
        if graphData:
            lines = graphData.split('\n')
            xs=[]
            ys=[]
            for line in lines:
                if len(line) > 1:
                    x,y = line.split(',')
                    xs.append(float(x))
                    ys.append(float(y))

                ax1.clear()
                ax1.plot(xs, ys)
                plt.axis([None, None, 0, 50])

    ani = animation.FuncAnimation(fig, myAnimateFunc, interval=1000)
    plt.show()


if __name__ == '__main__':
    main()
