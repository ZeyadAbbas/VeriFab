from verifab import *

clk = Input("clk")
data_in = Input("data_in", width=8, signed=False)
data_out = Output("data_out", width=16, signed=True, default=-10)
bus = InOut("bus", width=32, signed=True)

print(clk)
print(data_in)
print(data_out)
print(bus)
