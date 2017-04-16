
echo "Entered svd_post_formatting.sh ..."
num_layers=$1

# BASH function
line() { # selects a particular line
    head $1 $2 | tail -n 1; }

for i in $(seq 1 $num_layers)
do
    # weight matrix input to the linear layer
    nrows=$(wc -l N_$i | awk '{print $1}')  
    ncols=$(line -5 N_$i | tr ' ' '\n' | wc -l | awk '{print $1}')
    echo "N_$i has $nrows rows and $ncols cols"
    echo "<affinetransform> $nrows $ncols" > n 
    echo "[" >> n 
    cat N_$i >> n
    echo "]" >> n
    echo -n "[ " >> n
    str="" ; for j in $(seq 1 $nrows); do str="0 $str" ; done
    echo -n $str >> n 
    echo " ]" >> n
    echo "<linear> $nrows $nrows" >> n
 
    # weight matrix output from the linear layer
    nrows=$(wc -l U_$i | awk '{print $1}') 
    ncols=$(line -5 U_$i | tr ' ' '\n' | wc -l | awk '{print $1}')
    echo "U_$i has $nrows rows and $ncols cols"
    echo "<affinetransform> $nrows $ncols" > u
    echo "[" >> u
    cat U_$i >> u
    echo "]" >> u
    cat bias_$i >> u 
    if [ $i -ne $num_layers ]; then
       echo "<relu> $nrows $nrows" >> u 
    else
       echo "<softmax> $nrows $nrows" >> u 
    fi
 
    cat n u >> dnn.nnet.svd
done

echo "Exited svd_post_formatting.sh ..."
