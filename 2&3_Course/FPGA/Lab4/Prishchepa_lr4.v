module operation(x1, x2, x3, dnf, knf);
  input x1, x2, x3;
  output dnf;
  output knf;
  assign dnf = ~((x1 | x2) & (x1 | ~x3) & (x2 | ~x3));
  assign knf = ~(~(~x1 | ~x2) | ~(~x1 | x3) | ~(~x2 | x3));
endmodule

