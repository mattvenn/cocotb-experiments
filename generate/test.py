import cocotb

@cocotb.test()
async def test(dut):
    # test fails with this error:
    # AttributeError: top contains no object named genblk1
    # change False to True below to make the test pass
    if False:
        for thing in dut:
            pass

    print(dut.genblk1[0].sub_inst.clk.value)
