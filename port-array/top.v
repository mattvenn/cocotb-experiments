`default_nettype none

module top (
	input wire clk,
	output wire [1:0] trigger_array,
	output wire trigger
);

    reg value = 0;
    assign trigger_array = {value, value};

	always @(posedge clk)
        value <= ~value;

endmodule
