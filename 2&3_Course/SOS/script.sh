#!/bin/bash
nrows=$(grep -cE '^.*\s4[0-9][0-9]\s.*$' $1)
cat $1 | awk 'BEGIN{FS=" "}($9 ~ /^4[0-9][0-9]$/){print $11}' | sort | uniq -c | awk 'BEGIN{FS=" ";nrows='$nrows'}{print $2"\t"$1"\t"$1/nrows*100"%"}' | sort -k 3n | tail -10 | tac
