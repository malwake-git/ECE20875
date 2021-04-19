#!/usr/bin/env bash

V1=${OUTFILE}.out
echo $V1

V2=${OUTFILE}.err
echo $V2

./cmd1 < $INFILE | ./cmd3 1> $V1  2> $V2
