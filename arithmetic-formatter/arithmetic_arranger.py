# For a complete breakdown of the project and its requirements: https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter

import re

def arithmetic_arranger(problems, solved = False):
    # 5 problems maximum
    if len(problems) > 5:
      return "Error: Too many problems."

    # create create final return strings, set to empty
    first_num_string = ''
    second_num_string = ''
    line_string = ''
    sum_string = ''
    arranged_problems = ''
    # answer string depends on optional argument

    # iterate through input list
    for problem in problems:
      # if the current problem string contains anything that's not a number or +/-
      # operators, return error
      if (re.search('[^\s0-9+-]', problem)):
        if (re.search('[/]', problem) or re.search('[*]', problem)):
          return "Error: Operator must be '+' or '-'."
        return "Error: Numbers must only contain digits."
      # split the current problem on a space
      curr_problem = problem.split(' ')

      # create a length variable for the largest number length + 2
      length = max(len(curr_problem[0]), len(curr_problem[2])) + 2
      # if either of the numbers is longer than 4, return error
      if (length - 2) > 4:
        return "Error: Numbers cannot be more than four digits."

      # create helpful aliases
      first = curr_problem[0].rjust(length)
      operator = curr_problem[1]
      second = operator + (curr_problem[2].rjust(length - 1))
      lines = ''

      # add the appropriate number of dashes to the lines variable
      for i in range(length):
        lines += '-'

      # calculate the problem result
      if operator == '+':
        sum = str(int(first) + int(curr_problem[2])).rjust(length)
      else:
        sum = str(int(first) - int(curr_problem[2])).rjust(length)

      # assign each num and operator string to its appropriate line, adding appropriate
      # whitespace if the current problem is not the last
      if problem != problems[-1]:
        first_num_string += first + '    '
        second_num_string += second + '    '
        line_string += lines + '    '
        sum_string += sum + '    '
      else:
        first_num_string += first
        second_num_string += second
        line_string += lines
        sum_string += sum

    # return the arranged problems, with or without the solutions
    if solved == True:
      arranged_problems += first_num_string + '\n' + second_num_string + '\n' + line_string + '\n' + sum_string
    else:
      arranged_problems += first_num_string + '\n' + second_num_string + '\n' + line_string

    return arranged_problems