# For a complete breakdown of the project and its requirements: https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator

import math

def add_time(start, duration, start_day = None):

    # split the start time on a space and duration on a colon
    start_time = start.split(" ")
    start_hours = int(start_time[0].split(":")[0])
    start_minutes = int(start_time[0].split(":")[1])

    duration_hours = int(duration.split(":")[0])
    duration_minutes = int(duration.split(":")[1])

    # store the meridian in a variable for later reference
    start_meridian = start_time[1]

    # determine the minutes place result

    # if the minutes sum is > 60
    minutes_sum = start_minutes + duration_minutes
    # if the minutes sum > 60
    if minutes_sum >= 60:
      # divide by 60, round to a reasonable place, stringify, then split the quotient and remainder apart
      minutes = str(round(minutes_sum / 60, 10)).split(".")
      # multiply the remainder by 60 to get final minutes value. stringify for final return statement
      final_minutes = str(round(float("." + minutes[1]) * 60))
      # add a zero in front if final minute calculation is < 9
      if int(final_minutes) < 10:
        final_minutes = "0" + final_minutes
      # additional hours to be added to hours equation
      additional_hours = int(minutes[0])
    # if sum < 60, stringify for final return statement
    else:
      # add a zero in front if final minute calculation is < 9
      if int(minutes_sum) < 10:
        final_minutes = "0" + str(minutes_sum)
      else:
        final_minutes = str(minutes_sum)

      additional_hours = 0



    # add hours together
    hours_sum = start_hours + duration_hours + additional_hours

    # if hours sum is > 12, do the same as above, expect divide and multiply by 12
    if hours_sum % 12 == 0:
       final_hours = "12"
       total_meridians = int(hours_sum / 12)
    elif hours_sum > 12:
      hours = str(round(hours_sum / 12, 10)).split(".")
      final_hours = str(round(float("." + hours[1]) * 12))
      # this time the quotient is saved as the number of meridians, or 12-hour chunks that have passed
      total_meridians = int(hours[0])
    elif hours_sum < 12:
      # if the hours sum is < 12, represent it as is
      final_hours = str(hours_sum)
      total_meridians = 0


    # calculate the final meridian
    if (total_meridians % 2) == 0:
      final_meridian = start_meridian
    elif start_meridian == "AM":
      final_meridian = "PM"
    elif start_meridian == "PM":
      final_meridian = "AM"



    # use the whole number to determine the final meridian and the number of days that have passed

    # if the number of meridians is even, divide by two to get the number of days passed
    if total_meridians % 2 == 0:
      days_passed = int(total_meridians / 2)
    # else divide by two, round up if the starting meridian is PM and down if it is AM
    else:
      if start_meridian == "AM":
        # integer division here because I'm not allowed to import libraries and this needs to round down
        days_passed = int(total_meridians // 2)
      else:
        days_passed = total_meridians / 2
        if days_passed.is_integer():
          days_passed = int(days_passed)
        else:
          days_passed = int(days_passed + 1)

    # calculate the final day if a start_day argument has been provided
    if start_day:
      days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
      if days_passed > 7:
        days_divided = str(round(days_passed / 7, 10)).split(".")
        final_day = days_list[6 - (round(float("." + days_divided[1]) * 7))]
      elif (days_list.index(start_day.capitalize()) + days_passed) > 6:
        final_day = days_list[6 - days_passed]
      else:
        final_day = days_list[days_list.index(start_day.capitalize()) + days_passed]

    # prepare the statement indicating the number of passed days
    if days_passed == 0:
      days_passed = ""
    elif days_passed == 1:
      days_passed = " (next day)"
    else:
      days_passed = f" ({days_passed} days later)"

    # put everything together
    if start_day:
      final_time_string = f"{final_hours}:{final_minutes} {final_meridian}, {final_day}{days_passed}"
    else:
      final_time_string = f"{final_hours}:{final_minutes} {final_meridian}{days_passed}"

    return final_time_string