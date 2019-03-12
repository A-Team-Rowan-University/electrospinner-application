from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText, ControlSlider, ControlButton
#from .middlware import 

class UserInterface(BaseWidget):

    def __init__(self, *args, **kwargs):
        super().__init__('Electrospinner')

        #Definition of the forms fields
        self._temperature_goal = ControlSlider('Temperature Goal (F)', default=0, minimum=0, maximum=400)
        self._soak_time = ControlSlider('Temperature Goal (F)', default=0, minimum=0, maximum=400)
        self._runbutton     = ControlButton('Run')

def start_ui():
    from pyforms import start_app
    start_app(UserInterface)
