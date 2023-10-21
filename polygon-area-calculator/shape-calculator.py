# For a complete breakdown of the project and its requirements: https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator

class Rectangle:
  # define init function, should store height and width
  def __init__(self, width, height):
    self.width = width
    self.height = height

  # define string function to print custom string
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  # define set width and set height methods
  def set_width(self, new_width):
    self.width = new_width

  def set_height(self, new_height):
    self.height = new_height

  # get_area method
  def get_area(self):
    return self.width * self.height

  # get_perimiter method
  def get_perimeter(self):
    return (2 * self.width) + (2 * self.height)

  # get_diagonal method
  def get_diagonal(self):
    return ((self.width ** 2) + (self.height ** 2)) ** .5

  # get_picture method
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."

    line = ("*" * self.width) + "\n"

    picture = ""

    for n in range(self.height, 0, -1):
      picture += line

    return picture

  # get_amount_inside method
  def get_amount_inside(self, shape):
    # divide self area by shape area, return the quotient
    return self.get_area() // shape.get_area()


class Square(Rectangle):
  # init function, sets height and width to be the same value
  def __init__(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    return f"Square(side={self.width})"

  # define set_width, set_height, and set_side functions
  def set_width(self, new_width):
    self.width = new_width
    self.height = new_width

  def set_height(self, new_height):
    self.height = new_height
    self.width = new_height

  def set_side(self, new_side):
    self.height = new_side
    self.width = new_side
