input_digit macro
 mov ah, 9              ;showing a tip
 int 21h
 lea dx, inme           ;input a number
 mov ah, 10
 int 21h
 mov al,10              ;print a new line after the input
 int 29h
 mov al,13
 int 29h
endm

str_to_int macro inmes
local convert_loop, minus_check, convert_to_digit, add_digit, minimal_possible, error_1, error_2, finn, done
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
 cmp is_negative, 1       ;check if the number is negative
 jne done
 neg num
done:
 xor ch, ch
endm

result_print macro number
local m1, m2, m3
 mov bx, number
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
endm

result_print_dword macro summ
local m_1, m_2, m_3
.386
 mov ebx, summ
 or ebx, ebx
 jns m_1
 mov al, '-'
 int 29h
 neg ebx
m_1:
 mov eax, ebx
 xor cx, cx
 mov ebx, 10
m_2:
 xor edx, edx
 div ebx
 add dl, '0'
 push dx
 inc cx
 test eax, eax
 jnz m_2
m_3:
 pop ax
 int 29h
 loop m_3
endm

array_input macro
local elem_inp
.386
 lea dx, elements_tip         ;print a tip
 mov ah, 9
 int 21h                       
 mov al,10                    ;print a new line
 int 29h
 mov al,13
 int 29h
 mov counter, 0
 mov di, 0
elem_inp:                     ;input loop
 lea dx, el_tip               ;formatted input array element
 mov ah, 9
 int 21h
 result_print counter
 lea dx, el_input_tip
 input_digit
 str_to_int inme
 error_check
 mov ax, num
 mov [arr+di], ax
 inc counter
 add di, 2
 mov cx, counter
 cmp cx, arr_size
 jne elem_inp
endm

array_sum macro summ
local sum_loop
.386
 lea dx, sum_print
 mov ah, 9
 int 21h
 xor dx, dx
 xor ax, ax
 mov cx, arr_size
 mov di, 0
sum_loop:
 mov ax, [arr+di]
 cwde
 add edx, eax
 add di, 2
 loop sum_loop
 mov summ, edx
endm

array_min_and_max macro 
local read_num, set_new_min, set_new_max, exit
 mov ax, [arr]
 mov min, ax
 mov max, ax
 mov cx, arr_size
 sub cx, 1
 jcxz exit
 mov si, 2
read_num:
 mov ax, [arr+si]
 cmp ax, min
 jl set_new_min
 cmp ax, max
 jg set_new_max
 add si, 2
 loop read_num
 jmp exit
set_new_min:
 mov min, ax
 add si, 2
 dec cx
 jcxz exit
 jmp read_num
set_new_max:
 mov max, ax
 add si, 2
 dec cx
 jcxz exit
 jmp read_num
exit:
endm

array_sort macro
local outer_loop, inner_loop, continue, sort_done
 cmp arr_size, 1
 je sort_done
 mov si, 0
outer_loop:
 mov cx, arr_size
 dec cx
 mov di, 0
inner_loop:
 mov ax, [arr+di]         ;compare this element and next one
 cmp ax, [arr+di+2]
 jng continue
 mov dx, [arr+di]         ;swap elements if next one less
 mov ax, [arr+di+2]
 mov [arr+di], ax
 mov [arr+di+2], dx
continue:
 add di, 2
 loop inner_loop
 inc si
 cmp si, arr_size
 jl outer_loop
sort_done:
endm

array_print macro
local show
 lea dx, sorted_arr_print
 mov ah, 09h
 int 21h
 mov di, 0
 mov si, 0
show:
 result_print [arr+si]
 mov al, ' '
 int 29h
 add si, 2
 inc di
 cmp di, arr_size
 jne show
endm

exit macro
  mov AH, 4CH
  int 21H
endm

error_check macro
local raise_error_1, raise_error_2, contin
  cmp is_error, 1
  je raise_error_1
  cmp is_error, 2
  je raise_error_2
  jmp contin
raise_error_1:                  ;invalid symbol(s) error
  LEA dx, error_message_1
  MOV ah,9
  INT 21h
  exit
raise_error_2:                  ;wrong number error
  LEA dx, error_message_2
  MOV ah,9
  INT 21h
  exit
contin:
endm

check_interval macro st, en, number
local final, con
 cmp number, st
 jle final
 cmp number, en
 jg final
 jmp con
final:               
 LEA dx, error_message_2
 MOV ah,9
 INT 21h
 exit
con:
endm

STSEG SEGMENT PARA STACK "STACK"
DB 64 DUP("STACK")
STSEG ENDS

DSEG SEGMENT PARA PUBLIC "DATA"
arr_size dw 0
inme db 7,?,7 dup (" $")
el_tip db "The $"
el_input_tip db " element => $"
is_negative db 0
num dw 0
digit dw 0
is_error db 0
error_message_1 db "Invalid symbol(s)!$"
error_message_2 db "Number is out of diapason!$"
size_tip db "Enter the size of array (1-32) => $"
elements_tip db "Enter values in [-32768; 32767]:$"
arr dw 32 dup (?)
sum_print db "Total sum: $"
sum dd 0
min_print db 13,10, "Minimal element: $"
min dw 0
max_print db 13,10, "Maximal element: $"
max dw 0
sorted_arr_print db 13, 10, "Sorted array: $"
counter dw 0
DSEG ENDS

CSEG SEGMENT PARA PUBLIC "CODE"
ASSUME CS:CSEG, DS:DSEG, SS:STSEG

main proc
 mov ax, dseg
 mov ds, ax
 lea dx, size_tip         ;input and convert size of array
 input_digit
 str_to_int inme
 error_check
 check_interval 0, 32, num
 mov ax, num
 mov arr_size, ax
 array_input              ;entering array elements
 error_check
 array_sum sum            ;calculate and print the sum 
 result_print_dword sum
 array_min_and_max        ;find and print min and max element 
 lea dx, min_print
 mov ah, 9
 int 21h
 result_print min
 lea dx, max_print
 mov ah, 9
 int 21h
 result_print max
 array_sort               ;sort array and print it
 array_print
 exit
 ret
main endp

CSEG ENDS
end main