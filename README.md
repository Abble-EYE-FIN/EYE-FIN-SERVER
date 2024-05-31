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

Build Docker Image
```
docker build -t {image name} .
```

Run Docker Image
```
docker run -rm -p 8000:8000 {image name}:{tag}
```

### How To Start Server
1. Turn on Server PC
2. Press `ctrl + alt + t` then terminal will appear
3. `cd eye-fin/EYE-FIN-SERVER`
4. `python3 server.py`
5. Create another terminal and type in `ifconfig`
6. look for `wlan0` kind of stuff... this is the IP address

Main Server
```bash
python3 server.py
```
API Server
```bash
uvicorn app:app --host 0.0.0.0 --reload
```

### JSON Data Format
```json
{
    "reference" : {
        "ACC" :{"X" : x_data, "Y" : y_data, "Z" : z_data, },
        "GYR" :{"X" : x_data, "Y" : y_data, "Z" : z_data, },
        "MAG" :{"X" : x_data, "Y" : y_data, "Z" : z_data, },
    },
    "fin1" : {
        "ACC" :{"X" : x_data, "Y" : y_data, "Z" : z_data, },
        "GYR" :{"X" : x_data, "Y" : y_data, "Z" : z_data, },
        "MAG" :{"X" : x_data, "Y" : y_data, "Z" : z_data, },
    },
    "fin2" : {
        "ACC" :{"X" : x_data, "Y" : y_data, "Z" : z_data, },
        "GYR" :{"X" : x_data, "Y" : y_data, "Z" : z_data, },
        "MAG" :{"X" : x_data, "Y" : y_data, "Z" : z_data, },
    },
    "fin3" : {
        "ACC" :{"X" : x_data, "Y" : y_data, "Z" : z_data, },
        "GYR" :{"X" : x_data, "Y" : y_data, "Z" : z_data, },
        "MAG" :{"X" : x_data, "Y" : y_data, "Z" : z_data, },
    },
}
```

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
