    add    $t0, $gp, $zero      # &A[0] - 28
    lw     $t1, 4($s0)          # fetch N
    sll    $t1, $t1, 2          # N as byte offset
    add    $t1, $t1, $gp        # &A[N] - 28
    or     $t2, $zero, $s3      # MAX_SIZE
top:
    sltu   $t3, $t0, $t1        # have we reached the final address?
    beq    $t3, $zero, e      # yes, we're done
    add    $t0, $t0, $t5          # update $t0 to point to next element
    j      top                  # go to top of loop
e: