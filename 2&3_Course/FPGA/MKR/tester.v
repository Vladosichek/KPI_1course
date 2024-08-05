module tester;
  reg [4:0] Ain, Bin;
  reg Cin;
  wire [5:0] Sum;
  wire Cout;
  wire [5:0] Result;
  wire [3:0] Flags;

  Adder5bit uut (
    .Sum(Sum),
    .Cout(Cout),
    .Ain(Ain),
    .Bin(Bin),
    .Cin(Cin)
  );

  PostProcessor pp (
    .Result(Result),
    .Flags(Flags),
    .Sum(Sum),
    .Cout(Cout),
    .Ain(Ain),
    .Bin(Bin)
  );

  initial begin
    $monitor("Time: %0t | Ain = %b (%0d), Bin = %b (%0d), Cin = %b | Sum = %b (%0d), Cout = %b | Result = %b (%0d), Flags = %b", 
             $time, Ain, $signed(Ain), Bin, $signed(Bin), Cin, Sum, $signed(Sum), Cout, Result, $signed(Result), Flags);

    // New Test Case 1: Ain = 0, Bin = 0, Cin = 0
    Ain = 5'b00000; Bin = 5'b00000; Cin = 0; // 0 + 0 = 0
    #10;

    // New Test Case 2: Ain = 15, Bin = 1, Cin = 0
    Ain = 5'b01111; Bin = 5'b00001; Cin = 0; // 15 + 1 = 16
    #10;

    // New Test Case 3: Ain = -1, Bin = 1, Cin = 1
    Ain = 5'b11111; Bin = 5'b00001; Cin = 1; // -1 + 1 + 1 = 1
    #10;

    // New Test Case 4: Ain = 7, Bin = -8, Cin = 0
    Ain = 5'b00111; Bin = 5'b11000; Cin = 0; // 7 + (-8) = -1
    #10;

    // New Test Case 5: Ain = -4, Bin = -3, Cin = 1
    Ain = 5'b11100; Bin = 5'b11101; Cin = 1; // -4 + (-3) + 1 = -6
    #10;

    // New Test Case 6: Ain = 10, Bin = 10, Cin = 1
    Ain = 5'b01010; Bin = 5'b01010; Cin = 1; // 10 + 10 + 1 = 21 (Overflow)
    #10;

    // New Test Case 7: Ain = 3, Bin = -3, Cin = 0
    Ain = 5'b00011; Bin = 5'b11101; Cin = 0; // 3 + (-3) = 0
    #10;

    // New Test Case 8: Ain = 16, Bin = 16, Cin = 0
    Ain = 5'b10000; Bin = 5'b10000; Cin = 0; // 16 + 16 = 32 (Overflow)
    #10;

    $finish;
  end
endmodule
