#!/bin/bash
# Print the 10th line of file.txt
# If the file contains less than 10 lines, it should output nothing.
# There's at least three different solutions. Try to explore all possibilities.

# Author : Sanchez Vincent
# Email : vincent3426@bupt.edu.cn
# Date : 2016-01-11

sed -n '10p' file.txt

# head -10 file.txt | tail -n +10
# head -10 file.txt | tail -1 # When the file contains less than 10 lines, it outputs the last line instead of nothing.

# tail -n +10 file.txt | head -1