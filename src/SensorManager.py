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
        pass
    
    def _parse_message(self, message : str):
        self.msg_str = json.load(message)
        self.ref_msg= [[0]*3]*3
        self.fin_msg= []

        # parse all data from json message
        self._set_reference(self.msg_str["reference"])
        for i in range(3):
            self._set_fingers(self.msg_str[f"fin{i+1}"])

    
    def _set_reference(self, message):
        self.ref_msg= [[message["ACC"]["X"],message["ACC"]["Y"],message["ACC"]["Z"]],
                       [message["GYR"]["X"],message["GYR"]["Y"],message["GYR"]["Z"]],
                       [message["MAG"]["X"],message["MAG"]["Y"],message["MAG"]["Z"]]]
    
    # self.fin_msg[0] : fin1, self.fin_msg[1] : fin2, self.fin_msg[2] : fin3
    def _set_fingers(self, idx, message):
        self.fin_msg.append(
                            [[message["ACC"]["X"],message["ACC"]["Y"],message["ACC"]["Z"]],
                             [message["GYR"]["X"],message["GYR"]["Y"],message["GYR"]["Z"]],
                             [message["MAG"]["X"],message["MAG"]["Y"],message["MAG"]["Z"]]]
                            )
    
    def _make_decision(self, idx:int):
        target = self.fin_msg[idx]
        # do calculation with 'self.ref_msg'

        return 0 #or 1


    def interpreteMotion(self, message)->str:
        # all (1+3)*(3,3,3) data set in self variables
        self._parse_message(message=message)
        f1 : str = str(self._make_decision(0))
        f2 : str = str(self._make_decision(1))
        f3 : str = str(self._make_decision(2))
        return f1+f2+f3