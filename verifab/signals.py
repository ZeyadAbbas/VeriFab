class Signal:
    def __init__(self, name, bits=1, signed=False, default=0):
        self.name = name
        self.width = bits
        self.signed = signed
        self.value = default
        self.validate()

    def validate(self):
        min_val = -(2 ** (self.width - 1)) if self.signed else 0
        max_val = (2 ** self.width) - 1 if not self.signed else (2 ** (self.width - 1)) - 1

        if not (min_val <= self.value <= max_val):
            raise ValueError(
                f"Default value {self.value} is out of range for {self.width}-bit {'signed' if self.signed else 'unsigned'} signal.")

    def set_value(self, value):
        min_val = -(2 ** (self.width - 1)) if self.signed else 0
        max_val = (2 ** self.width) - 1 if not self.signed else (2 ** (self.width - 1)) - 1

        if not (min_val <= value <= max_val):
            raise ValueError(
                f"Value {value} is out of range for {self.width}-bit {'signed' if self.signed else 'unsigned'} signal.")

        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, width={self.width}, signed={self.signed}, value={self.value})"


class Input(Signal):
    def __init__(self, name, bits=1, signed=False):
        super().__init__(name, bits, signed, default=0)


class Output(Signal):
    def __init__(self, name, bits=1, signed=False, default=0):
        super().__init__(name, bits, signed, default)


class InOut(Signal):
    def __init__(self, name, bits=1, signed=False, default=0):
        super().__init__(name, bits, signed, default)
        self.high_impedance = True

    def set_high_impedance(self, state=True):
        self.high_impedance = state

    def __repr__(self):
        return f"{super().__repr__()}, high_impedance={self.high_impedance}"
