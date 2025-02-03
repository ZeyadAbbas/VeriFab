from signals import *


class Module:
    def __init__(self, name):
        self.name = name
        self.inputs = {}
        self.outputs = {}
        self.submodules = {}

    def add_input(self, input_signal):
        if not isinstance(input_signal, Input):
            raise TypeError("Expected an Input type.")
        self.inputs[input_signal.name] = input_signal

    def add_output(self, output_signal):
        if not isinstance(output_signal, Output):
            raise TypeError("Expected an Output type.")
        self.outputs[output_signal.name] = output_signal

    def add_submodule(self, submodule):
        if not isinstance(submodule, Module):
            raise TypeError("Expected a Module type.")
        self.submodules[submodule.name] = submodule

    def connect(self, output_signal, input_signal):
        if not isinstance(output_signal, Output) or not isinstance(input_signal, Input):
            raise TypeError("Connection must be between an Output and an Input.")
        input_signal.set_value(output_signal.value)

    def __repr__(self):
        return (f"Module(name={self.name}, inputs={list(self.inputs.keys())}, "
                f"outputs={list(self.outputs.keys())}, submodules={list(self.submodules.keys())})")
