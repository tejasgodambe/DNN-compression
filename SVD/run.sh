#!/bin/bash 

# Initial parameter setting
num_layers=4
cp dnn.nnet.bak dnn.nnet
[[ -e dnn.nnet.svd ]] && rm dnn.nnet.svd 

# BASH functions
block() { # selects a block of lines
  tail -n +$1 $3 | head -$(($2-$1+1)); }
line()  { # selects a particular line
  head $1 $2 | tail -n 1; }

# The 1st and 2nd args to block fn, and 1st arg to line fn
# has to be hard-coded
block 3 514 dnn.nnet > layer_1
block 520 775 dnn.nnet > layer_2
block 781 1292 dnn.nnet > layer_3
block 1298 2210 dnn.nnet > layer_4
line -516 dnn.nnet > bias_1
line -777 dnn.nnet > bias_2
line -1294 dnn.nnet > bias_3
line -2212 dnn.nnet > bias_4

# Child scripts are called  
python3 svd.py
bash svd_post_formatting.sh $num_layers

rm n u N_* U_*
