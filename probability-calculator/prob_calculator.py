import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key in kwargs.keys():
            for value in range(kwargs[key]):
                self.contents.append(key)
        self.balls_data = kwargs

    def draw(self, num):
        # balls = copy.deepcopy(self.contents)  # put this in the function instead?
        # no this removes balls from the list, gotta create a new list for balls drawn
        balls = list()
        balls_num = min(num, len(self.contents))
        for ball in range(balls_num):
            # balls.pop(random.randrange(len(balls)))
            index_ball = random.randint(0, len(self.contents)-1)
            balls.append(self.contents.pop(index_ball))
        return balls

    def __str__(self):
        string_repr = ",".join("{}={}".format(k, v) for k, v in self.balls_data.items())
        return string_repr


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for n in range(num_experiments):
        n_hat = copy.deepcopy(hat)
        n_balls = n_hat.draw(num_balls_drawn)

        sum_balls = dict()
        for ball in n_balls:
            sum_balls[ball] = sum_balls.get(ball, 0) + 1
        # print(sum_balls)
        # print(expected_balls)

        # compare the sum_balls to expected_balls, at least the same amount of each color
        similar = True
        for exp_color, exp_amount in expected_balls.items():
            if sum_balls.get(exp_color, 0) < exp_amount:
                similar = False
                break
        if similar == True:
            m += 1
            # for sum_amount in sum_balls.values():  #  sum_color,
            #     try:
            #         if sum_balls[] >= expected_balls[exp_color]:
            #             m += 1
            #     except Exception as e:
            #         print(e)

        # c_balls = []
        # for exp_color, exp_count in expected_balls.items():
            # c_balls += [exp_ball] * exp_count
            # if exp_count <= count(c_balls[exp_ball]):
            # print(exp_count, sum_balls[exp_color])
                    # m += 1
            #         print(successful_draw)

    return round(m/num_experiments, 3)

# if __name__ == "__main__":
#     hat1 = Hat(red=1, green=2, blue=3, purple=4)
#     print(hat1)
#     print(hat1.draw(4))
#     print(hat1.contents)
