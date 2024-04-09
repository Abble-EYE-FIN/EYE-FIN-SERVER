from utils.imports import *

@dataclass
class SensorData:
    acc : float
    gyro : float
    mag : float