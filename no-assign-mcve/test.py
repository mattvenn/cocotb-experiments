import cocotb
from cocotb.clock import Clock

@cocotb.test()
async def test1(dut):
    clock = Clock(dut.clk, 10, units="us")
    cocotb.fork(clock.start())
    dut.test <= 1

@cocotb.test()
async def test2(dut):
    clock = Clock(dut.clk, 10, units="us")
    cocotb.fork(clock.start())
    assert dut.test == 1
