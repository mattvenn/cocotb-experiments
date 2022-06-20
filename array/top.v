`default_nettype none

module top (
	input wire clk,
	output wire out_val
);

    `ifdef COCOTB_SIM
        initial begin
            $dumpfile ("top.vcd");
            $dumpvars (0, top);
            #1;
        end
    `endif

	localparam NUM = 2;

	reg val [0:NUM-1];
	assign out_val = val[0];

endmodule
