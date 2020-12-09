import types
from vistrails.core.modules.basic_modules import ModuleError


def get_input(self, port_name, allow_default=True):
    if port_name in self.inputPorts:
        if allow_default:  # removed self.registry boolean
            defaultValue = self.inputPorts[port_name][0].get_output("value")  # modified access to default value
            if defaultValue is not None:
                return defaultValue
        raise ModuleError(self, "Missing value from port %s" % port_name)


def mutate_method(obj, method_name, new_method):
    obj.__dict__[method_name] = types.MethodType(new_method, obj)