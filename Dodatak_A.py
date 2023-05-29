import os
import sys
import getpass
import unittest
import math

class OperationsManager():

    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def perform_division(self) -> float:
        """Divides a with b. If b is zero, returns NaN."""
        return self.a / self.b

def login_success():
    a = float(input("A = "))
    b = float(input("B = "))
    ops_manager = OperationsManager(a, b)
    print(ops_manager.perform_division())
 
    expression = input('Enter a mathematical formula to calculate: ')
    print ("Result: ", eval(expression))

class TestOperationsManager(unittest.TestCase):
    def test_div(self):
        ops = OperationsManager(6, 2)
        self.assertEqual(ops.perform_division(), 3)

    def test_div_0_by_num(self):
        ops = OperationsManager(0, 5)
        self.assertEqual(ops.perform_division(), 0)

    def test_div_by_0(self):
        ops = OperationsManager(3, 0)
        retval = ops.perform_division()
        self.assertTrue(math.isnan(retval))

    def test_div_0_by_0(self):
        ops = OperationsManager(0, 0)
        retval = ops.perform_division()
        self.assertTrue(math.isnan(retval))

if __name__ == "__main__":
    user = input("Username: ")
    password = getpass.getpass("Password: ")
    if user != "root" or password != "123":
        print("Wrong username or password!")
        exit(0)
    else:
        print("Login success!")
        login_success()
