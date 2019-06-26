
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
    recordFile = "myData.txt"

    def __init__(self, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True  # Daemonize thread

        thread.start()  # Start the execution

    def appendMeasurement(self, timestamp, temp, boardId):
        # debug print
        print("Timestamp: %f \tDevice: %s -> Temperatura: %.2f" % (timestamp, boardId, temp))
        with open(self.recordFile, 'a+') as myFile:
            myFile.write("%f,%f,%s\n" % (timestamp, temp, boardId))

    def run(self):
        print("***BLE sniffer***")
        scanner = Scanner()
        startTime = time.time()

        if os.path.exists(self.recordFile):
            os.remove(self.recordFile)
        os.mknod(self.recordFile)

        while True:
            devices = scanner.scan(0.5)

            for dev in devices:
                for (adtype, desc, value) in dev.getScanData():

                    # skip if adv type is not Manufacturer data or length is not 5 bytes
                    if adtype != 0xFF or len(value) != 10:
                        break

                    # string + little endian
                    tempStr = value[8] + value[9] + value[6] + value[7] + value[4] + value[5] + value[2] + value[3]

                    # string to hex
                    temp = (struct.unpack('!f', bytes.fromhex(tempStr))[0])

                    # get timestamp
                    timestamp = time.time() - startTime

                    if (value[0] + value[1]) == 'ab':
                        self.appendMeasurement(timestamp, temp, 'nRF52832')

                    if (value[0] + value[1]) == 'cd':
                        self.appendMeasurement(timestamp, temp, 'nRF52840')


