;logical XNOR operations
;output displayed using 7447 IC

.include "/home/meghana/m328Pdef.inc"

ldi r16, 0b00111100 ;identifying output pins 2,3,4,5
out DDRD,r16		;declaring pins as output



ldi r16,0b00000001	;initializing W
ldi r17,0b00000001	;initializing X
;logical XNOR
eor r16,r17			    ; XOR W,X
ldi r23,0b00000001
eor r23,r16         ; XNOR
;following code is for displaying output
;shifting LSB in r16 to 2nd position
ldi r20, 0b00000010	;counter = 2

rcall loopw		;calling the loopw routine

out PORTD,r23		;writing output to pins 2,3,4,5


Start:
rjmp Start

;loop for bit shifting
loopw:	lsl r23			;left shift
	dec r20			;counter --
	brne loopw	;if counter != 0
	ret
