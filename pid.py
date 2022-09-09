from globalVariables import MAX_THRUST

# PID Gain
KP = 0.8
KD = 1.5
KI = 0

class PID(object):
    def __init__(self, target, KP = KP, KI = KI, KD = KD):
        self.kp = KP
        self.ki = KI
        self.kd = KD
        self.setpoint = target-12
        self.error = 0
        self.integral_error = 0
        self.error_last = 0
        self.derivative_error = 0
        self.output = 0
    def setTarget(self, target):
        self.setpoint = target-12
    def compute(self, pos, time):
        if(time <= 0 ):
            return 0
        self.error = self.setpoint - pos
        self.integral_error += self.error * time
        self.derivative_error = (self.error - self.error_last) / time
        self.error_last = self.error
        self.output = self.kp*self.error + self.ki * self.integral_error + self.kd * self.derivative_error
        if self.output > 0:
            self.output = 0
        if self.output < -MAX_THRUST:
            self.output = -MAX_THRUST
        return self.output 