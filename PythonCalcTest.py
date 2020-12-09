#!/usr/bin/env python2.7
import unittest
from helper_functions import mutate_method, get_input
from vistrails.core.modules.basic_modules import Float, String
from vistrails.packages.pythonCalc.init import PythonCalc


class TestPythonCalc(unittest.TestCase):
    def setUp(self):
        self.python_calc = PythonCalc()
        mutate_method(self.python_calc, "get_input", get_input)

        self.f1, self.f2, self.s1 = Float(), Float(), String()
        self.f1.setValue(8.0)
        self.f2.setValue(2.0)

    
    def assign_parameters(self):
        self.python_calc.set_input_port("value1", self.f1) #entry 1 for PythonCalc box
        self.python_calc.set_input_port("value2", self.f2) #entry 2 for PythonCalc box
        self.python_calc.set_input_port("op", self.s1)     #entry 3 for PythonCalc box
    
    def test_addition(self):
        self.s1.setValue('+')
        self.assign_parameters()
        self.python_calc.compute()
        self.assertEqual(self.python_calc.get_output("value"), 10.0) #output for PythonCalc box

    def test_subtraction(self):
        self.s1.setValue('-')
        self.assign_parameters()
        self.python_calc.compute()
        self.assertEqual(self.python_calc.get_output("value"), 6.0)

    def test_division(self):
        self.s1.setValue('/')
        self.assign_parameters()
        self.python_calc.compute()
        self.assertEqual(self.python_calc.get_output("value"), 4.0)

    def test_multiplication(self):
        self.s1.setValue('*')
        self.assign_parameters()
        self.python_calc.compute()
        self.assertEqual(self.python_calc.get_output("value"), 16.0)


if __name__ == "__main__":
    unittest.main()