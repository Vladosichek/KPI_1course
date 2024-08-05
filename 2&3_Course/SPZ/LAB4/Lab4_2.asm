STSEG SEGMENT PARA STACK "STACK"
DB 64 DUP("STACK")
STSEG ENDS

DSEG SEGMENT PARA PUBLIC "DATA"
n dw 0        ;rows
m dw 0        ;columns
inmes db 7,?,7 dup (" $")
matr_tip db "Element [$"
matr_i_tip db "][$"
matr_ij_tip db "] => $"
is_negative db 0
num dw 0
digit dw 0
is_error db 0
error_message_1 db "Invalid symbol(s)!$"
error_message_2 db "Number is out of range!$"
n_input_tip db "Ammount of rows (1-16) => $"
m_input_tip db "Ammount of columns (1-16) => $"
el_input_tip db "Enter values in [-32768; 32767]:$"
arr dw 16 dup (16 dup (?))
i dw 0
j dw 0
value_entr_tip db "Enter seeken value => $"
no_entries_found db "There are no entries!$"
con_query db "Find any other value? ('y'-continue, else - stop) => $"
is_in_matrix db 0
tmp dw 0
DSEG ENDS

CSEG SEGMENT PARA PUBLIC "CODE"
ASSUME CS:CSEG, DS:DSEG, SS:STSEG

main proc
 mov ax, dseg
 mov ds, ax
 lea dx, n_input_tip                    ;input row number
 call input_digit
 call str_to_int
 cmp is_error, 1
 je raise_error_1
 cmp is_error, 2
 je raise_error_2
 cmp num, 0
 jle raise_error_2
 cmp num, 16
 jg raise_error_2
 mov ax, num
 mov n, ax
 lea dx, m_input_tip                    ;input column number 
 call input_digit
 call str_to_int
 cmp is_error, 1
 je raise_error_1
 cmp is_error, 2
 je raise_error_2
 cmp num, 0
 jle raise_error_2
 cmp num, 16
 jg raise_error_2
 mov ax, num
 mov m, ax
 call matr_input                        ;entering matrix elements
 cmp is_error, 1
 je raise_error_1
 cmp is_error, 2
 je raise_error_2
 call find_entries_dialog               ;seeking of elment coordinates
 jmp end_program
raise_error_1:
 LEA dx, error_message_1
 MOV ah,9
 INT 21h
 jmp end_program
raise_error_2:
 LEA dx, error_message_2
 MOV ah,9
 INT 21h
end_program:
 mov AH, 4CH
 int 21H
 ret
main endp

input_digit proc
 mov ah, 9              ;showing a tip
 int 21h
 lea dx, inmes          ;input a number
 mov ah, 10
 int 21h
 mov al,10              ;print a new line after the input
 int 29h
 mov al,13
 int 29h
 ret
input_digit endp

str_to_int proc
 mov num, 0
 mov is_negative, 0
 mov si, offset inmes + 2 ;load the address of the first element
 mov ch, 0
convert_loop:
 mov ax, 0                ;check if it is the end of inmes
 mov al, inmes + 1
 cmp al, ch
 je finn
 mov al, [si]             ;set element of inmes to al
 cmp al, '0'
 jl minus_check           ;check if the character is between "0" and "9"
 cmp al, '9'
 jg error_1
 inc ch
 inc si                   
 jmp convert_to_digit     ;go to next element in inmes
minus_check:              ;check character for "-"
 cmp al, '-'
 jne error_1
 cmp ch, 0                ;check if it is the first element in inmes
 jne error_1
 mov is_negative, 1
 inc ch
 inc si
 jmp convert_loop
convert_to_digit:
 sub al, '0'
 mov digit, ax
 mov bx, 10
 mov ax, num
 mul bx
 jc error_2
 js error_2
 mov num, ax
 mov ax, digit
 cmp num, 32760
 je minimal_possible
add_digit:
 add num, ax
 jc error_2
 js error_2
 jmp convert_loop
minimal_possible:
 cmp is_negative, 0
 je add_digit
 neg num
 sub num, ax
 jo error_2
 jmp done
error_1:
 mov is_error, 1
 jmp done
error_2:
 mov is_error, 2
 jmp done
finn:
 cmp is_negative, 1       
 jne done
 neg num
done:
 xor ch, ch
 ret
str_to_int endp

result_print proc
 mov bx, num
 or bx, bx
 jns m1
 mov al, '-'
 int 29h
 neg bx
m1:
 mov ax, bx
 xor cx, cx
 mov bx, 10
m2:
 xor dx, dx
 div bx
 add dl, '0'
 push dx
 inc cx
 test ax, ax
 jnz m2
m3:
 pop ax
 int 29h
 loop m3
 ret
result_print endp

matr_input proc
 lea dx, el_input_tip                ;print a tip
 mov ah, 9
 int 21h
 mov al,10                           ;print a new line after the input
 int 29h
 mov al,13
 int 29h
 mov di, 0
element_input:                       ;input loop
 lea dx, matr_tip                    ;formatted input and convert matrix element
 mov ah, 9
 int 21h
 mov ax, i
 inc ax
 mov num, ax
 call result_print
 mov num, 0
 lea dx, matr_i_tip
 mov ah, 9
 int 21h
 mov ax, j
 inc ax
 mov num, ax
 call result_print
 mov num, 0
 lea dx, matr_ij_tip
 call input_digit
 call str_to_int
 cmp is_error, 1
 je end_input
 cmp is_error, 2
 je end_input
 mov ax, num
 mov [arr+di], ax
 add di, 2
 inc j
 mov cx, j                           ;if end of row, go to next row
 cmp cx, m
 jl element_input
 mov j, 0
 inc i
 mov bx, i
 mov ax, 32
 mul bl
 mov di, ax
 cmp bx, n                           ;if end of last row, end input
 jl element_input
end_input:
 ret
matr_input endp

find_entries_dialog proc
dialog_loop:
 mov is_error, 0                             
 mov is_in_matrix, 0
 lea dx, value_entr_tip
 call input_digit
 call str_to_int
 cmp is_error, 1
 je no_such_values
 cmp is_error, 2
 je no_such_values
 call find_and_print_entries                 ;procedure to find and print entered value's entries
 cmp is_in_matrix, 0                         ;print that no entries of entered value if it wasn`t found
 je no_such_values
continue_dialog:
 lea dx, con_query                           ;ask user if he wants to continue searching for values' entries
 call input_digit
 mov dl, [inmes+2]
 cmp dl, 'y'
 je dialog_loop
 jne end_proc
no_such_values:
 lea dx, no_entries_found
 mov ah, 9
 int 21h
 mov al,10                                   ;print a new line after the input
 int 29h
 mov al,13
 int 29h
 jmp continue_dialog
end_proc:
 ret
find_entries_dialog endp

find_and_print_entries proc
 mov ax, num
 mov tmp, ax
find_entries:
 mov i, 0                                        ;clear needed variables and registers
 mov j, 0
 mov di, 0
matr_loop:                                       ;loop through matrix elements
 mov dx, [arr+di]
 cmp dx, tmp
 je print_coordinates
raise_ij:                                        ;changing variables so that we check next matrix element
 add di, 2
 inc j
 mov cx, j
 cmp cx, m                                       ;if end of row, go to next row
 jl matr_loop
 mov j, 0
 inc i
 mov bx, i
 mov ax, 32
 mul bl
 mov di, ax
 cmp bx, n                                       ;if end of last row, end procedure
 jl matr_loop
 ret
print_coordinates:                               ;print i and j indexes of value which entries are being found
 mov is_in_matrix, 1
 lea dx, matr_tip
 mov ah, 9
 int 21h
 mov ax, i
 inc ax
 mov num, ax
 call result_print
 lea dx, matr_i_tip
 mov ah, 9
 int 21h
 mov ax, j
 inc ax
 mov num, ax
 call result_print
 mov al, ']'
 int 29h
 mov al,10                                       ;print a new line after the input
 int 29h
 mov al,13
 int 29h
 jmp raise_ij
find_and_print_entries endp

CSEG ENDS
end main