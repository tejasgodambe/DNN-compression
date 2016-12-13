import sys
import numpy as np

print ('Entered svd.py ...')

layers = ['layer_1', 'layer_2', 'layer_3', 'layer_4'] 
nsing_vals = [112, 117, 124, 232] 

for i in range(len(layers)):
   layer = np.loadtxt(layers[i])
   u, s, v = np.linalg.svd(layer, full_matrices=True)
   U=u[:,0:nsing_vals[i]]
   V=v[0:nsing_vals[i],:]
   s=s[0:nsing_vals[i]]
   S=np.diag(s)
   N=np.matmul(S,V)
   np.savetxt('U_' + str(i+1), U)
   np.savetxt('N_' + str(i+1), N)

print ('Exited svd.py ...')

#print (s.shape)
#Sum = np.sum(s)
#percent_60 = 0.90 * Sum 
#percent_70 = 0.95 * Sum 
#percent_80 = 0.98 * Sum
#percent_90 = 0.99 * Sum
#total = 0
#count = 0
#ticked_90 = 0
#ticked_80 = 0
#ticked_70 = 0
#ticked_60 = 0
#for x in np.nditer(s):
#   total = total + x
#   count = count + 1
#   if total >= percent_90 and ticked_90 == 0: 
#      print (str(count) + ' makes up 90%')
#      ticked_90 = 1 
#   elif total >= percent_80 and ticked_80 == 0: 
#      print (str(count) + ' makes up 80%') 
#      ticked_80 = 1 
#   elif total >= percent_70 and ticked_70 == 0: 
#      print (str(count) + ' makes up 70%') 
#      ticked_70 = 1 
#   elif total >= percent_60 and ticked_60 == 0: 
#      print (str(count) + ' makes up 60%') 
#      ticked_60 = 1 
#   else: 
#      pass
#
#
