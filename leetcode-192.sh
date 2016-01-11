#!/bin/bash
# Read from the file words.txt and output the word frequency list to stdout.
# words.txt contains only lowercase characters and space ' ' characters.
# Each word must consist of lowercase characters only.
# Words are separated by one or more whitespace characters.

# Author : Sanchez Vincent
# Email : vincent3426@bupt.edu.cn
# Date : 2016-01-11

cat $1 | sed 's/^[ \t]*//' | tr -cs "[a-z][A-Z]" "\n" | sort | uniq -c | sort -k1nr -k2 | sed 's/^[ \t]*//'  | awk -F'[ ]' '{print $2,$1}'

