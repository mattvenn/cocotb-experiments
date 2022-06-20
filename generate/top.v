`default_nettype none

module top (
	input wire clk
);

	localparam NUM = 2;

	generate
		genvar i;
		for(i = 0; i < NUM; i = i + 1) begin
			sub sub_inst(.clk(clk));
		end
	endgenerate

endmodule

module sub (
	input wire clk
);

endmodule
