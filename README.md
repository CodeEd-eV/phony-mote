# phony-mote
Remotely control your computer with another device. Can be phone, tablet or other devices that are able to open a website.

The interface of the remote is shown below. If there is anyone willing to improve the interface, please let me know! Feel free to submit pull requests!

# Remote Setup
![](fig/output2.gif)
------------------
# Remote Streaming mode (experimental)
![](fig/output.gif)

## Getting started
1. ``git clone git@github.com:CodeEd-eV/phony-mote.git``
2. ``cd phony-mote``
3. ``pipenv shell``
3. ``./start``
4. enjoy!

## How it works
1. A webserver is hosted on the computer.
2. The remote device and the computer need to be in the same network, so that the webserver is accessible for the remote.
3. The remote can then access the website through the network, e.g. `192.168.0.1:8088`
4. The website shows a few buttons that will trigger keystrokes on the computer.
5. control computer via remote!
