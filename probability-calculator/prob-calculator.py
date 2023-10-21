# For a complete breakdown of the project and its requirements: https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator

import copy
import random
# Consider using the modules imported above.

class Hat:
  # define init function that creates 'contents' list variable
  def __init__(self, **kwargs):
    self.contents = []
    # append string of color name to contents in an amount equal to the passed in value
    for key in kwargs:
      for n in range(kwargs[key], 0, -1):
        self.contents.append(key)

    # print('init:', self.contents)

  # draw method
  def draw(self, draws):

    # return contents if the number of draws exceeds length of contents list
    if draws >= len(self.contents):
      return self.contents

    # create a result list that balls will be added to
    result = []

    # iterate through n number of draws
    for n in range(draws, 0, -1):
      # use random module to generate a pseudo-random index number within the range of list length
      rand_index = random.choice(range(0, len(self.contents)))
      # remove the element at that index, adding it to the result list
      drawn_ball = self.contents.pop(rand_index)
      result.append(drawn_ball)

    # return the result list
    return result



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  # create a success count variable
  success_count = 0
  # iterate through the number of required experiments
  for n in range(num_experiments):
    # create boolean flag, set to true
    flag = True
    # copy the input hat object
    hat_copy = copy.deepcopy(hat)

    # use the draw method to return a list of drawn balls
    draw_result = hat_copy.draw(num_balls_drawn)

    # create a histogram of the drawn balls and compare to expected balls
    ball_count = dict()

    for ball in draw_result:
      ball_count[ball] = ball_count.get(ball, 0) + 1

    # if the drawn balls dict matches the expected balls dict
    for key in expected_balls:

      if key not in ball_count or ball_count[key] < expected_balls[key]:
        flag = False
        break

    # increment the success count
    if flag:
      success_count += 1

  return success_count / num_experiments