import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge


@cocotb.test()
async def test(dut):
    clock = Clock(dut.clk, 10, units="us")
    cocotb.fork(clock.start())
    
    await RisingEdge(dut.clk)
    dut.val[0] <= 0
    await RisingEdge(dut.clk)
    dut.val[0] <= 1
    await RisingEdge(dut.clk)
    dut.val[0] <= 0
    await RisingEdge(dut.clk)
