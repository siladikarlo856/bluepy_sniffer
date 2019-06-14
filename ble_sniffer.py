#!/usr/bin/env python

from bluepy.btle import Scanner, DefaultDelegate
import time
import os

import struct

def main():
    print("***BLE sniffer***")
    scanner = Scanner()
    startTime = time.time()

    if os.path.exists("myData.txt"):
        os.remove("myData.txt")


    while(True):
        devices = scanner.scan(1.0)

        for dev in devices:
            if dev.addr == 'd7:d1:6a:27:c7:c8':
                for (adtype, desc, value) in dev.getScanData():
                    value = value[6] + value[7] + value[4] + value[5] +value[2] +value[3]+ value[1]+ value[2]
                    temp = (struct.unpack('!f', bytes.fromhex(value))[0])
                    print("nRF52-DK Temperatura:  %f" % (temp))


            if dev.addr == 'da:0b:5e:4f:af:97':
                for (adtype, desc, value) in dev.getScanData():
                    value = value[6] + value[7] + value[4] + value[5] +value[2] +value[3]+ value[1]+ value[2]
                    temp = (struct.unpack('!f', bytes.fromhex(value))[0])
                    timestamp = time.time() - startTime
                    print("Timestamp: %f " % timestamp)
                    print("nRF52840-DK Temperatura:  %f" % (temp))

                    with open("myData.txt", 'a+') as myFile:
                        myFile.write("%f,%f\n" %(timestamp, temp))


if __name__ == "__main__":
    main()

