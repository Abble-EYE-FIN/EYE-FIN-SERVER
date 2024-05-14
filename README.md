# EYE-FIN-SERVER
## Linux Server System Repo
### prerequisitories
Install python packages
```
sudo apt update 
sudo apt install -y mosquitto
sudo systemctl restart mosquitto
sudo apt install -y mosquitto-clients

pip3 install -r requirements.txt
```
!! Need to open port !!
```
# add these lines on /etc/mosquitto/mosquitto.conf
listener 1883
allow_anonymous true
```

### How To Start Server
1. Turn on Raspberry pi
2. Press `ctrl + alt + t` then terminal will appear
3. `cd eye-fin/EYE-FIN-SERVER`
4. `python3 mainserver.py`
5. Create another terminal and type in `ifconfig`
6. look for `wlan0` kind of stuff... this is the IP address


### SYSTEM Diagram
![EF_SYS_DIA](https://github.com/Abble-EYE-FIN/EYE-FIN-SERVER/assets/68832065/8518dad6-f417-4aed-b2e5-2aba2abd5e48)

### Test Methods
Publish
```
mosquitto_pub -h localhost -t righthand/input -m "testmessage1"
```
Subscribe
```
mosquitto_sub -h localhost -t righthand/input
```

### Progress Report
