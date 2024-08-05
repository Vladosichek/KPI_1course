module PostProcessor(Result, Flags, Sum, Cout, Ain, Bin);
  output [5:0] Result;
  output [3:0] Flags; // N, Z, C, V
  input [5:0] Sum;
  input Cout;
  input [4:0] Ain, Bin;
  
  wire N, Z, C, V;

  assign N = Sum[5]; // Знаковий розряд
  assign Z = (Sum == 6'b000000);
  assign C = Cout;
  assign V = (Ain[4] & Bin[4] & ~Sum[5]) | (~Ain[4] & ~Bin[4] & Sum[5]); // Переповнення у знаковому розряді

  assign Flags = {N, Z, C, V};

  // Нормалізація у випадку переповнення
  assign Result = (V) ? {Sum[5], Sum[5:1]} : Sum;

endmodule

