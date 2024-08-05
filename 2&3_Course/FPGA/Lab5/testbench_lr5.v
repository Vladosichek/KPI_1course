`timescale 1ns / 1ps

module testbench_lr5;
    reg [3:0] D;
    reg A0;
    reg A1;
    reg A2;
    wire [3:0] Q0;
    wire [3:0] Q1;
    wire [3:0] Q2;
    wire [3:0] Q3;
    wire [3:0] Q4;

    lr5_Prishchepa uut (
        .D(D),
        .A0(A0),
        .A1(A1),
        .A2(A2),
        .Q0(Q0),
        .Q1(Q1),
        .Q2(Q2),
        .Q3(Q3),
        .Q4(Q4)
    );

    initial begin
        $monitor("Time = %0d A2 = %b A1 = %b A0 = %b D = %b Q0 = %b Q1 = %b Q2 = %b Q3 = %b Q4 = %b",
                 $time, A2, A1, A0, D, Q0, Q1, Q2, Q3, Q4);
        
        // Випадок 1
        A2 = 0; A1 = 0; A0 = 0; D = 4'b1010; #10;
        // Випадок 2
        A2 = 0; A1 = 0; A0 = 1; D = 4'b1100; #10;
        // Випадок 3
        A2 = 0; A1 = 1; A0 = 0; D = 4'b1110; #10;
        // Випадок 4
        A2 = 0; A1 = 1; A0 = 1; D = 4'b0001; #10;
        // Випадок 5
        A2 = 1; A1 = 0; A0 = 0; D = 4'b0111; #10;
        
        $finish;
    end
endmodule

