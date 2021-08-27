# WAY 1
# It is the module name
import turtle

# Turtle() is the name of the class
tim = turtle.Turtle()
# ______________________________

# WAY 2
# it avoid have to write every time turtle.Turtle()
from prettytable import PrettyTable
# from prettytable import *  => it should be avoid

table = PrettyTable()
# _______________________________

# WAY 3
# It is the module name with an alias
import turtle as t

# Turtle() is the name of the class
rock = t.Turtle()
# ______________________________

# To import additional modules not included in python library you should install the module as with pretty table
# PYPI
