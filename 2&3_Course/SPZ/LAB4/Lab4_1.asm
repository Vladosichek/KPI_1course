STSEG SEGMENT PARA STACK "STACK"
DB 64 DUP("STACK")
STSEG ENDS

DSEG SEGMENT PARA PUBLIC "DATA"
arr_size dw 0
inmes db 7,?,7 dup (" $")
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
 call input_digit
 call str_to_int
 cmp is_error, 1          
 je raise_error_1
 cmp is_error, 2          
 je raise_error_2
 cmp num, 0
 jle raise_error_2
 cmp num, 32
 jg raise_error_2
 mov ax, num
 mov arr_size, ax
 call array_input         ;entering array elements
 cmp is_error, 1          
 je raise_error_1
 cmp is_error, 2          
 je raise_error_2
 call array_sum           ;calculate and print the sum 
 call result_print_dword
 call array_min_and_max   ;find and print min and max element 
 lea dx, min_print
 mov ah, 9
 int 21h
 mov ax, min
 mov num, ax
 call result_print
 lea dx, max_print
 mov ah, 9
 int 21h
 mov ax, max
 mov num, ax
 call result_print
 call array_sort         ;sort array and print it
 call array_print
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
 cmp is_negative, 1       ;check if the number is negative
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

result_print_dword proc
.386
 mov ebx, sum
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
 ret
result_print_dword endp

array_input proc
 lea dx, elements_tip         ;print a tip
 mov ah, 9
 int 21h                       
 mov al,10                    ;print a new line
 int 29h
 mov al,13
 int 29h
 mov counter, 0
 mov di, 0
element_input:                ;input loop
 lea dx, el_tip               ;formatted input array element
 mov ah, 9
 int 21h
 mov ax, counter
 mov num, ax
 call result_print
 lea dx, el_input_tip
 call input_digit
 call str_to_int
 cmp is_error, 1               
 je end_input
 cmp is_error, 2
 je end_input
 mov ax, num
 mov [arr+di], ax
 inc counter
 add di, 2
 mov cx, counter
 cmp cx, arr_size
 jne element_input
end_input:
 ret
array_input endp

array_sum proc
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
 mov sum, edx
 ret
array_sum endp

array_min_and_max proc
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
 ret
array_min_and_max endp

array_sort proc
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
 ret
array_sort endp

array_print proc
 lea dx, sorted_arr_print
 mov ah, 09h
 int 21h
 mov di, 0
 mov si, 0
show:
 mov dx, [arr+si]
 mov num, dx
 call result_print
 mov al, ' '
 int 29h
 add si, 2
 inc di
 cmp di, arr_size
 jne show
 ret
array_print endp

CSEG ENDS
end main