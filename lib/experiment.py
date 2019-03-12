from datetime import timedelta

class Experiment:

    def __init__(self):

        self.draw_rate = -1
        self.temperature_goal = -1
        self.soak_time = timedelta(seconds=-1)

        self.DRAW_RATE_MIN = 0
        self.DRAW_RATE_MAX = 100

        self.TEMPERATURE_MIN = 0
        self.TEMPERATURE_MAX = 500

        self.SOAK_TIME_MIN = timedelta(seconds=0)
        self.SOAK_TIME_MAX = timedelta(days=99)

    def reset(self):
        # TODO: clean up
        self.draw_rate = -1
        self.temperature_goal = -1
        self.soak_time = timedelta(seconds=-1)

    def is_valid(self):
        return (
            self.DRAW_RATE_MIN <= self.draw_rate <= self.DRAW_RATE_MAX and
            self.TEMPERATURE_MIN <= self.temperature_goal <= self.TEMPERATURE_MAX and
            self.SOAK_TIME_MIN <= self.soak_time <= self.SOAK_TIME_MAX
        )

    @property
    def draw_rate(self):
        return self.__draw_rate

    @draw_rate.setter
    def draw_rate(self, draw_rate):
        self.__draw_rate = draw_rate

    @property
    def temperature_goal(self):
        return self.__temperature_goal

    @temperature_goal.setter
    def temperature_goal(self, temperature_goal):
        self.__temperature_goal = temperature_goal
