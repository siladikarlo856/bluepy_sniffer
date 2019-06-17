from bluepy.btle import Scanner
import threading
import time
import os

import struct

class BleSnifferThread(object):
    """
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True  # Daemonize thread

        thread.start()  # Start the execution

    def run(self):
        print("***BLE sniffer***")
        scanner = Scanner()
        startTime = time.time()

        if os.path.exists("myData.txt"):
            os.remove("myData.txt")
        os.mknod("myData.txt")

        while True:
            devices = scanner.scan(0.1)

            for dev in devices:
                if dev.addr == 'd7:d1:6a:27:c7:c8':
                    for (adtype, desc, value) in dev.getScanData():
                        value = value[6] + value[7] + value[4] + value[5] + value[2] + value[3] + value[1] + value[2]
                        temp = (struct.unpack('!f', bytes.fromhex(value))[0])
                        timestamp = time.time() - startTime
                        print("Timestamp: %f nRF52-DK Temperatura:  %f" % (timestamp, temp))

                        with open("myData.txt", 'a+') as myFile:
                            myFile.write("%f,%f,%s\n" %(timestamp, temp, 'nRF52832'))

                if dev.addr == 'da:0b:5e:4f:af:97':
                    for (adtype, desc, value) in dev.getScanData():
                        value = value[6] + value[7] + value[4] + value[5] + value[2] + value[3] + value[1] + value[2]
                        temp = (struct.unpack('!f', bytes.fromhex(value))[0])
                        timestamp = time.time() - startTime
                        print("Timestamp: %f nRF52840-DK Temperatura:  %f" % (timestamp, temp))

                        with open("myData.txt", 'a+') as myFile:
                            myFile.write("%f,%f,%s\n" %(timestamp, temp, 'nRF52840'))
