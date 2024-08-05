input_digit macro

;input a string
  lea dx, inar
  mov ah, 10
  int 21h

;print a new line after the input
  mov al,10
  int 29h
  mov al,13
  int 29h
endm

str_to_int macro inarr
local convert_loop, check_minus, convert_to_digit, error_1, error_2, last, finish

;load the address of first element of the array
  mov si, offset inarr + 2 
  mov cx, 0

;check if inarr is empty
  mov ax, 0
  mov al, inarr + 1
  cmp al, 0
  je error_1

;converting of the array into number
  convert_loop:

;check if it is the end of inarr
    mov ax, 0
    mov al, inarr + 1
    cmp al, cl
    je last

;set element of inarr to al
    mov al, [si] 
  
;check if the character is between "0" and "9"
    cmp al, '0'
    jl check_minus
    cmp al, '9'
    jg error_1
    inc cx
    inc si   

;jump for converting character to digit
    jmp convert_to_digit 

;check character for "-"
  check_minus:
    cmp al, '-'
    jne error_1

;check if it is the first element in inarr
    cmp cx, 0
    jne error_1
    mov is_negative, 1
    inc cx
    inc si
    jmp convert_loop

;converting character to digit
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
    add num, ax
    jc error_2
    js error_2
    jmp convert_loop

;Used wrong symbol(s)
  error_1:
    mov is_error, 1
    jmp finish

;Inputed number out of range
  error_2:
    mov is_error, 2
    jmp finish

;check if the number is negative
  last:
    cmp is_negative, 1
    jne finish
    neg num

  finish:
endm

calc_res macro xpar
local x_zero, x_less, error, finishs

;compare xpar with 0
  cmp xpar, 0
  je x_zero
  jl x_less

;xpar>0 z=5*(4*xpar+7)/((xpar+1)*(xpar+2))
  mov ax, xpar
  add ax, 1
  jc error
  mov bx, ax
  add ax, 1
  jc error
  mul bx
  jc error
  mov denom, ax
  mov ax, xpar
  mov bx, 4
  mul bx
  jc error
  add ax, 7
  jc error
  mov bx, 5
  mul bx
  jc error
  mov bx, denom
  div bx
  mov num, ax
  mov ax, dx
  mov nom, ax
  jmp finishs

;xpar=0 z=5
  x_zero:
    mov ax, 5
    mov num, ax
    jmp finishs

;xpar<0 z=5*xpar^2/(1-xpar)
  x_less:
    mov ax, xpar
    neg ax
    jo error
    add ax, 1
    jc error
    mov denom, ax
    sub ax, 1
    mov bx, ax
    mul bx
    jc error
    mov bx, 5
    mul bx
    jc error
    mov bx, denom
    div bx
    mov num, ax
    mov ax, dx
    mov nom, ax
    jmp finishs

;xpar out of diapason
  error:
    mov is_error, 2

  finishs:
endm

result_print macro number
local m1, m2

;prepare to split number into digits
  mov ax, number
  xor cx, cx
  mov bx, 10

;split it into digits and write it down
  m1:
    xor dx, dx
    div bx
    add dl, '0'
    push dx
    inc cx
    test ax, ax
    jnz m1

;print these digits in correct order
  m2:
    pop ax
    int 29h
    loop m2
endm

exit macro

    mov AH, 4CH
    int 21H
endm

error_check macro
local raise_error_1, raise_error_2, continue

  cmp is_error, 1
  je raise_error_1
  cmp is_error, 2
  je raise_error_2
  jmp continue

;invalid symbol(s) error
  raise_error_1:
    LEA dx, error_message_1
    MOV ah,9
    INT 21h
    exit

;wrong number error
  raise_error_2:
    LEA dx, error_message_2
    MOV ah,9
    INT 21h
    exit

  continue:
endm

res_fraction macro
local frac, end_p

;printing of the result
  cmp num, 0
  je frac
  result_print num
  mov al, ' '
  int 29h

  cmp nom, 0
  jne frac
  jmp end_p

;printing of the fraction
  frac:
    result_print nom
    mov al, '/'
    int 29h
    result_print denom
  
  end_p:
endm

STSEG SEGMENT PARA STACK "STACK"
DB 64 DUP("STACK")
STSEG ENDS

DSEG SEGMENT PARA PUBLIC "DATA"
x dw 0
nom dw 0
denom dw 0
inar db 7,?,7 dup (" $")
input_tip db 13, 10, "Enter x in [-114;-1], {0} or [1;254] ==> $"
is_negative db 0
num dw 0
digit dw 0
is_error db 0
error_message_1 db "Invalid symbol(s)!$"
error_message_2 db "Number out of diapason!$"
DSEG ENDS

CSEG SEGMENT PARA PUBLIC "CODE"
ASSUME CS:CSEG, DS:DSEG, SS:STSEG

main proc

;ds initialisation
  mov ax, dseg
  mov ds, ax

;showing a tip
  lea dx, input_tip
  mov ah, 9
  int 21h

;input of number
  input_digit
  str_to_int inar
  error_check

;calculation
  mov ax, num
  mov x, ax
  calc_res x
  error_check
  res_fraction
  exit
  ret
main endp

CSEG ENDS
END MAIN