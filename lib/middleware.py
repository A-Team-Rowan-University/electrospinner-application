from pyserial import Serial
from experiment import Experiment
from user_interface import UserInterface


'''Provides logic to run main program'''
class Middleware:
    '''
    The Middleware class the main program logic that executes to run
    experiments and serves as the bridge between the other electrical and
    software components
    '''
    def __init__(self):
        # TODO: define init
        self.experiment = Experiment()
        self.serial = Serial(port='/dev/ttyACM0')
        pass

    def start_experiment(self):
        # TODO: define start_experiment
        # TODO: verify parameters
        pass

    def __set_motor(self,motor_speed_bytes):
        self.serial.write(motor_speed_bytes)
        pass
