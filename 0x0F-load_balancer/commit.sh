#!/bin/bash
# add, commit and push in one line
# arg1: files or . for all, arg2: message to commit
git add "$1"; git commit -am "$2"; git push
