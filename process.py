from vistrails.core.modules.basic_modules import Float, String
from vistrails.packages.pythonCalc.init import PythonCalc
from vistrails.core.modules.vistrails_module import ModuleConnector
from helper_functions import mutate_method, get_input


pythonCalc = PythonCalc()
f1, f2, s1 = Float(), Float(), String()

mutate_method(pythonCalc, "get_input", get_input)


f1.setValue(5.0)
f2.setValue(3.0)
s1.setValue('+')

pythonCalc.set_input_port("value1", f1)
pythonCalc.set_input_port("value2", f2)
pythonCalc.set_input_port("op", s1)


pythonCalc.compute()
print(pythonCalc.get_output("value"))