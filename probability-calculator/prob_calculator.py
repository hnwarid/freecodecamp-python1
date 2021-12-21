import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def name(self):
        pass

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass

if __name__ == "__main__":
    pass