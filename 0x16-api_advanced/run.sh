#!/bin/bash

test=$1
arg=$2

python3 tests/"$test" "$arg"

