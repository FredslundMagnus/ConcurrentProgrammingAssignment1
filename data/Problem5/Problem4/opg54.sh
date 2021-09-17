#!/bin/bash
# Read a string with spaces using for loop
for value in 10 100 1000
do
    for value1 in 1 2 4 8 16
    do
        java Search -W 10 -R 100 Chromosome.txt "ATATGTTTT" $value $value1 >> threads-$value1-tasks-$value.txt
    done
done
