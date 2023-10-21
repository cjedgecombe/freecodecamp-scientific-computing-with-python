# For a complete breakdown of the project and its requirements: https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app

import math

class Category:

  # define constructor function
  def __init__(self, category):
    # add category name variable, set to empty string
    self.name = category
    # add ledger variable, set to empty list
    self.ledger = []

  # define custom string method to return string of category transactions
  def __str__(self):
    # ^ operator will center the preceeding value (self.name) in * characters
    title = f"{self.name:*^30}\n"
    transactions = ""
    total = 0
    for trans in self.ledger:
      # take the first 23 characters of the description, right justify the amount 7 spaces and allow for 2 decial places
      item = f"{trans['description'][0:23]:23}" + f"{trans['amount']:>7.2f}\n"
      transactions += item

      total += trans["amount"]

    return title + transactions + f"Total: {total}"


  # define deposit method
  def deposit(self, amount, description = ""):
    deposit_obj = {"amount": amount, "description": description}
    self.ledger.append(deposit_obj)

  # define withdraw method
  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      withdrawal_obj = {"amount": (amount * -1), "description": description}
      self.ledger.append(withdrawal_obj)
      return True
    else:
      return False

  # define get balance method
  def get_balance(self):
    balance = 0
    for trans in self.ledger:
      balance += trans["amount"]
    return balance


  # define transfer method
  def transfer(self, amount, recipient):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {recipient.name}")
      recipient.deposit(amount, f"Transfer from {self.name}")
      return True
    else:
      return False

  # define check funds method
  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True

# define helper function for getting the total amount of spent money (this will help when generating the spend chart)
def get_total_spent(ledger):
  total = 0
  for trans in ledger:
    if trans["amount"] < 0:
      total += trans["amount"]
  return (total * -1)



def create_spend_chart(categories):
  # define heading string
  heading = "Percentage spent by category\n"

  grand_total = 0
  cats = []


  for cat in categories:
    total = get_total_spent(cat.ledger)
    cats.append({"name": cat.name, "total": total})
    grand_total += total

  # determine the percentage value of the total that each category spending total makes up
  # simplify that percentage to a rounded-down single-digit value (divide cat total by spending total, multiply by 100, round down to nearest whole number)
  # find someway to add the final percentage values to cat_totals object, maybe change the name
  # in the for loop below:
    # add an 'o' to each line

  for dict in cats:
    total = dict["total"]
    dict["perc"] = math.floor((total / grand_total) * 10) * 10

  graph = ""
  dash_count = (len(cats) * 2) + (len(cats) + 1)
  dashes = f"{('-' * dash_count).rjust(dash_count + 4)}\n"
  longest_name = 0
  names = ""

  for n in range(100, -1, -10):
    bars = ""
    for cat in cats:
      if n <= cat["perc"]:
        bars += "o  "
        cat["perc"] -= 10
      else:
        bars += "   "
    graph += f"{str(n) + '|':>4} {bars}\n"

  # determine the length of the longest category name
  for cat in cats:
    if len(cat["name"]) > longest_name:
      longest_name = len(cat["name"])

  # iterate through cats one more time to generate name section
  for n in range(longest_name, 0, -1):
    s = ""
    for cat in cats:
      if len(cat["name"]) != 0:
        s += f"{cat['name'][0]}  "
        cat["name"] = cat["name"][1:]
      else:
        s += "   "
    if n == 1:
      names += s.rjust(dash_count + 4)
    else:
      names += s.rjust(dash_count + 4) + "\n"

  return heading + graph + dashes + names