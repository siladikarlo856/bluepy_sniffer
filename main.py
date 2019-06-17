#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from ble_sniffer import *

def main():
    #style.use('fivethirtyeight')

    print("TENG BLE sniffer")

    # start BLE scanner in background
    BleSnifferThread()

    fig = plt.figure()
    fig.canvas.set_window_title('TENG BLE Sniffer')
    fig.suptitle("TENG temperature logger")

    ax1 = fig.add_subplot(111)
    plt.axis([None, None, 0, 50])
    plt.xlabel('Vrijeme [s]')
    plt.ylabel('Temperatura [°C]')

    def myAnimateFunc(i):
        graphData = open('myData.txt', 'r').read();
        if graphData:
            lines = graphData.split('\n')
            xs840=[]
            ys840=[]
            xs832=[]
            ys832=[]
            for line in lines:
                if len(line) > 1:
                    x,y,t = line.split(',')
                    if t == 'nRF52840':
                        xs840.append(float(x))
                        ys840.append(float(y))
                    if t == 'nRF52832':
                        xs832.append(float(x))
                        ys832.append(float(y))

                ax1.clear()
                ax1.plot(xs840, ys840, 'bo-', xs832, ys832, 'ro-')
                ax1.legend(['nRF52840', 'nRF52832'])
                plt.axis([None, None, 0, 50])
                plt.xlabel('Vrijeme [s]')
                plt.ylabel('Temperatura [°C]')

    ani = animation.FuncAnimation(fig, myAnimateFunc, interval=1000)

    plt.show()


if __name__ == '__main__':
    main()
