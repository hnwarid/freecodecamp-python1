import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key in kwargs.keys():
            for value in range(kwargs[key]):
                self.contents.append(key)
        self.balls_dict = kwargs


    def draw(self):
        pass

    def __str__(self):
        string_repr = ",".join("{}={}".format(k, v) for k, v in self.balls_dict.items())
        # string_repr = []
        # for key, value in self.kwargs.items():
        #
        #
        # string_repr = " ".join(string_repr)
        return string_repr


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass
    hats = Hat(hat)
    expected = expected_balls
    m = num_balls_drawn
    n = num_experiments
    print(hats, expected, m, n)

if __name__ == "__main__":
    hat1 = Hat(blue=1, red=3)
    print(hat1)