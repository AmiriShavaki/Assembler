fact:
     addi $sp, $sp, -8 # adjust stack for 2 items
     sw $ra, 4($sp) # save return address
     sw $a0, 0($sp) # save argument
     slti $t0, $a0, 1 # test for n < 1
     beq $t0, $zero, ELSE
     addi $v0, $zero, 1 # if so, result is 1
     addi $sp, $sp, 8 # pop 2 items from stack
     j $ra # and return to after jal
ELSE: addi $a0, $a0, -1 # n >= 1: argument gets (n - 1)
     jal fact # call fact with (n - 1)
     lw $a0, 0($sp) # restore original n
     lw $ra, 4($sp) # and return address
     addi $sp, $sp, 8 # pop 2 items from stack
     j $ra # and return to the caller
sll $t2, $t0, 4
or $t2, $t2, $t1
sll $t2, $t0, 4
andi $t2, $t2, -1
sra $t2, $t0, 3
andi $t2, $t2, 65519
sw $t1, 32($t2)
addi $t1, $0, $0
LOOP: lw $s1, 0($s0)
add $s2, $s2, $s1
addi $s0, $s0, 4