#!/bin/sh
echo "========================================================================"
input=$1
echo "[RUNNING]       :   "$input
while IFS= read -r line
do
    echo "========================================================================"
    echo "[INPUT]         : $line"
    python api.py "$line"
    echo "========================================================================"
done < "$input"
