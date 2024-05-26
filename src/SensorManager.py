# ESP imu data * (1+1) LR
# MPU imu data on each fingers * (3+3) LR
# ESP shall be reference, calculate relative angle (3mpu 1esp)
# checkout threshold -> binary checkup

# ex) 010 -> a : display in any way --> actuator
# to fast api server, subscribing app
# 'utf-8' string

from utils.imports import *

class SensorManager:
    _flag:str

    def __init__(self) -> None:
        self.ref_msg= [] # [[0]*3]*3
        self.fin_msg= []
        pass
    
    # message manager for MQTT json format
    def _parse_message(self, message : str):
        self.msg_str = json.load(message)

        # parse all data from json message
        self._set_reference(self.msg_str["reference"])
        self.fin_msg.clear()
        for i in range(3):
            self._set_fingers(self.msg_str[f"fin{i+1}"])
    
    # message manager for direct http conn
    def _parse_message_http(self, item):
        self.ref_msg_http= [[0]*3]*3
        self.fin_msg_http= []

        # parse all data
        self._set_reference_http(item.reference)
        self.fin_msg.clear()
        self._set_fingers_http(item.finger1)
        self._set_fingers_http(item.finger2)
        self._set_fingers_http(item.finger3)

    def _set_reference(self, message):
        self.ref_msg.clear()
        self.ref_msg= [[message["ACC"]["X"],message["ACC"]["Y"],message["ACC"]["Z"]],
                       [message["GYR"]["X"],message["GYR"]["Y"],message["GYR"]["Z"]],
                       [message["MAG"]["X"],message["MAG"]["Y"],message["MAG"]["Z"]]]
    
    def _set_reference_http(self, message: list):
        self.ref_msg.clear()
        self.ref_msg = [[message[0], message[1],message[2]],
                             [message[3], message[4],message[5]],
                             [message[6],message[7],message[8]]]
    
    # self.fin_msg[0] : fin1, self.fin_msg[1] : fin2, self.fin_msg[2] : fin3
    def _set_fingers(self, idx, message):
        self.fin_msg.append(
                            [[message["ACC"]["X"],message["ACC"]["Y"],message["ACC"]["Z"]],
                             [message["GYR"]["X"],message["GYR"]["Y"],message["GYR"]["Z"]],
                             [message["MAG"]["X"],message["MAG"]["Y"],message["MAG"]["Z"]]]
                            )
        
    def _set_fingers_http(self, message: list):
        self.fin_msg.append([[message[0], message[1],message[2]],
                                  [message[3], message[4],message[5]],
                                  [message[6],message[7],message[8]]]
        )

####### common interpreter ########
    def _make_decision(self, idx:int):
        target = self.fin_msg[idx]
        # do calculation with 'self.ref_msg'

        return 0 #or 1

    def interpreteMotion(self, mode:int, message)->str:
        # all (1+3)*(3,3,3) data set in self variables
        if mode == 0: # MQTT
            self._parse_message(message=message)
        elif mode == 1: # HTTP
            self._parse_message_http(item=message)

        f1 : str = str(self._make_decision(0))
        f2 : str = str(self._make_decision(1))
        f3 : str = str(self._make_decision(2))
        return f1+f2+f3