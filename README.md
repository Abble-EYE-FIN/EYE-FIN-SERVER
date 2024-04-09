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
### How To Start Server
1. Turn on Raspberry pi
2. Press `ctrl + alt + t` then terminal will appear
3. `cd eye-fin/EYE-FIN-SERVER`
4. `python3 mainserver.py`


### SYSTEM Diagram
![EF_SYS_DIA](https://github.com/Abble-EYE-FIN/EYE-FIN-SERVER/assets/68832065/8518dad6-f417-4aed-b2e5-2aba2abd5e48)

### Progress Report
- **240407** : SERVER 단에서 subscribe, return pubilsher 구현 완료. 9일 센서데이터 수령 이후 후처리 계획 설정 예정