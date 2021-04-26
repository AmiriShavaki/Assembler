fact:
     addi $sp, $sp, -8 # adjust stack for 2 items
     sw $ra, 4($sp) # save return address
     sw $a0, 0($sp) # save argument
     slti $t0, $a0, 1 # test for n < 1
     beq $t0, $zero, ELSE
     addi $v0, $zero, 1 # if so, result is 1
     addi $sp, $sp, 8 # pop 2 items from stack
     jr $ra # and return to after jal
ELSE: addi $a0, $a0, -1 # n >= 1: argument gets (n - 1)
     jal fact # call fact with (n - 1)
     lw $a0, 0($sp) # restore original n
     lw $ra, 4($sp) # and return address
     addi $sp, $sp, 8 # pop 2 items from stack
     mul $v0, $a0, $v0 # multipy to get result
     jr $ra # and return to the caller