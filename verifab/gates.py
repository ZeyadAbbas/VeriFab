from module import *


class AndGate(Module):
    def __init__(self, name, num_inputs=2):
        super().__init__(name)
        self.num_inputs = num_inputs
        for i in range(num_inputs):
            self.add_input(Input(f"A{i}"))
        self.add_output(Output("Y"))

    def evaluate(self):
        result = 1
        for inp in self.inputs.values():
            result &= inp.value
        self.outputs["Y"].set_value(result)


class OrGate(Module):
    def __init__(self, name, num_inputs=2):
        super().__init__(name)
        self.num_inputs = num_inputs
        for i in range(num_inputs):
            self.add_input(Input(f"A{i}"))
        self.add_output(Output("Y"))

    def evaluate(self):
        result = 0
        for inp in self.inputs.values():
            result |= inp.value
        self.outputs["Y"].set_value(result)
