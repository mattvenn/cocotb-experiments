import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, ClockCycles


@cocotb.test()
async def test(dut):
    clock = Clock(dut.clk, 10, units="us")
    cocotb.fork(clock.start())

#    dut.invert_in <= 0;
    dut.test <= 0;
    await ClockCycles(dut.clk, 20)
#    dut.invert_in <= 1;
    dut.test <= 1;
    await ClockCycles(dut.clk, 20)
