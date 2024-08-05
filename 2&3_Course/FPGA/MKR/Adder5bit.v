module Adder5bit(Sum, Cout, Ain, Bin, Cin);
  output [5:0] Sum;
  output Cout;
  input [4:0] Ain, Bin;
  input Cin;
  
  wire [4:0] c; // Внутрішні з'єднання для переносів

  // Перший розряд
  FullAdder fa0 (Sum[0], c[0], Ain[0], Bin[0], Cin);

  // Другий розряд
  FullAdder fa1 (Sum[1], c[1], Ain[1], Bin[1], c[0]);

  // Третій розряд
  FullAdder fa2 (Sum[2], c[2], Ain[2], Bin[2], c[1]);

  // Четвертий розряд
  FullAdder fa3 (Sum[3], c[3], Ain[3], Bin[3], c[2]);

  // П'ятий розряд
  FullAdder fa4 (Sum[4], c[4], Ain[4], Bin[4], c[3]);

  // Знаковий розряд (6-й розряд)
  FullAdder fa5 (Sum[5], Cout, Ain[4], Bin[4], c[4]);

endmodule

module FullAdder(sum, c_out, a, b, c_in);
  output sum, c_out;
  input a, b, c_in;
  wire s1, c1, c2;

  xor(s1, a, b);
  and(c1, a, b);
  xor(sum, s1, c_in);
  and(c2, s1, c_in);
  or(c_out, c2, c1);
endmodule

