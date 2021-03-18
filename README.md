# Bluepy BLE Sniffer
Scans BLE advertisment and deserialize it. Real-time temperature plote with matplotlib. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.




### Prerequisites

Run this command in terminal so python can use bluetooth without sudo permissions. 

```
sudo setcap 'cap_net_raw,cap_net_admin+eip' <bluepy-helper PATH>
```
To find bluepy-helper PATH just run the following command.

```
find /usr/ -name bluepy-helper

```

### Installing

For Python 3, you use pip3:
```
$ sudo apt-get install python3-pip libglib2.0-dev
$ sudo pip3 install bluepy
$ sudo pip3 install matplotlib
```

## Built With

Python 3


## Authors

***Karlo Siladi*** siladikarlo856@gmail.com


## Acknowledgments
* [bluepy by Ian Harvey](https://github.com/IanHarvey/bluepy)
