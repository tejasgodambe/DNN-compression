# DNN-compression

This code is the implementation of the paper "Restructuring of Deep Neural 
Network Acoustic Models with Singular Value Decomposition" 
(https://www.microsoft.com/en-us/research/wp-content/uploads/2013/01/svd_v2.pdf). 

# Basic idea
DNN weight matrices are usually sparse. This property can be exploited to 
represent a weight matrix with fewer values thus saving storage space and 
computations. Using singular value decomposition (SVD), 
a weight matrix is decomposed into product of two smaller matrices, 
that is, one weight layer is decomposed into cascade of two sub-layers. 
The first sub-layer carries linear activation function and zero bias, 
while the second sub-layer carries the activation function and bias values of 
the original decomposed layer. More details can be found in the paper. 

# Scripts
1. run.sh  
This is the master script. 
It takes dnn.nnet.bak file and produces dnn.nnet.svd file. 
Sample dnn.nnet.bak and dnn.nnet.svd files are provide for reference.
Set the values of the identifier num_layers, 2nd and 3rd arg of block 
function, first arg for line function according to your dnn.nnet.bak file. 

2. svd.py  
This python script is called by run.sh. It performs the actual SVD operation to
split the layers into two sub-layers. 

3. svd_post_formatting.sh  
This bash script is called by run.sh. It does the post formatting to 
construct the final dnn.nnet.svd file for us. 
