import time
import threading
import  ble_sniffer
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import  style

def main():
    style.use('fivethirtyeight')

    print("TENG BLE sniffer")

    #bleSnifferThread = threading.Thread(ble_sniffer.main())
    #bleSnifferThread.start()

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)

    def myAnimateFunc(i):
        graphData = open('myData.txt', 'r').read();
        lines = graphData.split('\n')
        xs=[]
        ys=[]
        for line in lines:
            if len(line) > 1:
                x,y = line.split(',')
                xs.append(float(x))
                ys.append(float(y))
                print(("%f,%f")%(float(x),float(y)))

            ax1.clear()
            ax1.plot(xs, ys)
            plt.axis([None, None, 0, 50])

    ani = animation.FuncAnimation(fig, myAnimateFunc, interval=1000)
    plt.show()


if __name__ == '__main__':
    main()
