	ADDI $5, $2, #10
	ORI $7, $2, #4
	ANDI $8, $3, #3
	LW $9, $31, #24
	NOP ;delay;
	NOP ;delay;
	NOP ;delay;
	SW $9, $31, #13 
	SLTI $10, $1, #20 
	BEQ $2, $10, #1 
	ADDI $11, $4, #1 
	ADDI $12, $4, #2
	ADDI $13, $4, #3
	ADDI $14, $4, #4
	ADDI $15, $4, #5 
	ADDI $16, $4, #6
	BEQ $4, $9, BEQLABEL
	NOP ;branch delay    ;
	NOP ;branch delay    ;
	NOP ;branch delay    ;
JUMPADDI:
	ADDI $17, $4, #7 
	J JUMPSALIDA
	NOP ;branch delay    ;
	NOP ;branch delay    ;
	NOP ;branch delay    ;
	NOP ;branch delay    ;
BEQLABEL:
	ADDI $18, $4, #8    
	ADDI $19, $4, #9     
	J JUMPADDI
	NOP ;branch delay    ;
	NOP ;branch delay    ;
	NOP ;branch delay    ;
	NOP ;branch delay    ; 
JUMPSALIDA:
	ADDI $20, $4, #10
	ADD $22, $4, $0 
	ADD $23, $4, $23 
	SUB $24, $2, $1 
	SUB $25, $1, $2
	AND $26, $3, $4
	OR  $27, $4, $3
	AND $28, $3, $10
	OR  $29, $7, $8
	SLT $30, $3, $4
	SLT $21, $1, $2
	NOP
	NOP
	NOP
	NOP