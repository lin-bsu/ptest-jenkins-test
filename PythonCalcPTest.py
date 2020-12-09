#!/usr/bin/env python2.7
from ptest import config
from ptest.plogger import preporter
from ptest.assertion import assert_equals
from ptest.decorator import TestClass, Test, BeforeMethod, AfterMethod
from helper_functions import mutate_method, get_input
from vistrails.core.modules.vistrails_module import ModuleError
from vistrails.core.modules.basic_modules import Float, String
from vistrails.packages.pythonCalc.init import PythonCalc


@TestClass(run_mode="parallel")
class PythonCalcTest:
    @BeforeMethod(enabled=True, description="Preparing instances and mutation.")
    def before(self):
        preporter.info("Initializing PythonCalc.")
        self.python_calc = PythonCalc()

        preporter.info("Mutating get_input method for PythonCalc instance.")
        mutate_method(self.python_calc, "get_input", get_input)

        preporter.info("Initializing constants and assigning values.")
        self.f1, self.f2, self.s1 = Float(), Float(), String()
        self.f1.setValue(8.0)
        self.f2.setValue(2.0)

    def assign_parameters(self):
        self.python_calc.set_input_port("value1", self.f1)
        self.python_calc.set_input_port("value2", self.f2)
        self.python_calc.set_input_port("op", self.s1)
    
    @Test(tags=["math"])
    def test_addition(self):
        self.s1.setValue('+')
        self.assign_parameters()
        self.python_calc.compute()
        assert_equals(self.python_calc.get_output("value"), 10.0)

    @Test(tags=["math"])
    def test_subtraction(self):
        self.s1.setValue('-')
        self.assign_parameters()
        self.python_calc.compute()
        assert_equals(self.python_calc.get_output("value"), 6.0)

    @Test(tags=["math"])
    def test_division(self):
        self.s1.setValue('/')
        self.assign_parameters()
        self.python_calc.compute()
        assert_equals(self.python_calc.get_output("value"), 4.0)

    @Test(tags=["math"])
    def test_multiplication(self):
        self.s1.setValue('*')
        self.assign_parameters()
        self.python_calc.compute()
        assert_equals(self.python_calc.get_output("value"), 16.0)
    
    @Test(tags=["math", "error"], expected_exceptions=(ZeroDivisionError,))
    def test_divide_by_zero(self):
        self.s1.setValue('/')
        self.f2.setValue(0)
        self.assign_parameters()
        self.python_calc.compute()

    @Test(tags=["math", "error"], expected_exceptions=(ModuleError,))
    def test_invalid_op(self):
        self.s1.setValue('Q')
        self.assign_parameters()
        self.python_calc.compute()
        
    @Test(tags=["math", "error"], expected_exceptions=(ValueError,))
    def test_invalid_set_1(self):
        preporter.info("Invalid value assigned to Float object.")
        self.f1.setValue("B")

    @Test(tags=["math", "error"], expected_exceptions=(AssertionError,))
    def test_invalid_set_2(self):
        preporter.info("Invalid value assigned to String object.")
        self.s1.setValue(1)

    @Test(tags=["math", "error"], expected_exceptions=(ValueError,))
    def test_invalid_set_3(self):
        preporter.info("Invalid value assigned to Float object.")
        self.f2.setValue("A")

    @AfterMethod(always_run=True, description="Clean up")
    def after(self):
        preporter.info("Finished.")

