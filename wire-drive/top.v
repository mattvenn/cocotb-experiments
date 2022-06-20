`default_nettype none

module top (
	input wire clk
);

    wire test = invert_in;
    wire invert_in;
    wire invert_out;

    `ifdef COCOTB_SIM
        initial begin
            $dumpfile ("top.vcd");
            $dumpvars (0, top);
            #1;
        end
    `endif

    in_out in_out0 (.clk(clk), .i(invert_in), .o(invert_out)); 

endmodule

module in_out (
    input wire clk,
    input wire i,
    output wire o
    );

    assign o = !i;

endmodule
