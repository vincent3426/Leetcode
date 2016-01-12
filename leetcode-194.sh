#!/bin/bash
# Read from the file file.txt and print its transposed content to stdout.
# I think any solution using pipe or other command combaination tech won't pass. 
# Only one-command solution (like awk) and pure bash solution seem to work.
# The real limit might be the number of subprocesses instead of memory.
# I don't think bash associative array (psuedo two-dimension array) use less memory, but it passed.

# Author : Sanchez Vincent
# Email : vincent3426@bupt.edu.cn
# Date : 2016-01-12

awk '{
    for(i = 1; i <= NF; i++)
        vector[NR, i] = $i
} END {
    for(i = 1; i <= NF; i++){
        line = vector[1, i]
        for(j = 2; j <= NR; j++)
            line = line" "vector[j, i]
        print line
    }
}' $1
