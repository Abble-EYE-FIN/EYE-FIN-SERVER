# EYE-FIN-SERVER
## Linux Server System Repo

!!! Do not run step1 unless it's initial setup
### Step1. prerequisitories
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

### Step2. How To Start Server
1. Turn on Server PC
2. Press `ctrl + alt + t` then terminal will appear
3. make two terminals
4. `cd eye-fin/EYE-FIN-SERVER`
5. type in `source braille/bin/activate` on both # <-- activate virtual environment>

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
