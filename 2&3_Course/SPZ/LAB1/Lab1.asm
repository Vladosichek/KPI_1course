stseg segment para stack "stack"
db 64 dup ("stack")
stseg ends

dseg segment para public "data"
source db 10, 20, 30, 40
dest db 4 dup ("?")
dseg ends

cseg segment para public "code"
main proc far
assume cs: cseg, ds: dseg, ss: stseg
;adress of return
push ds
mov ax, 0
push ax
;initialisation of ds
mov ax, dseg
mov ds, ax
; clearing of the array
mov dest, 0
mov dest+1, 0
mov dest+2, 0
mov dest+3, 0
; sending
mov al, source
mov dest+3, al
mov al, source+1
mov dest+2, al
mov al, source+2
mov dest+1, al
mov al, source+3
mov dest, al

ret
main endp
cseg ends
end main