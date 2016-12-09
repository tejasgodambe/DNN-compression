#

print (s.shape)
Sum = np.sum(s)
percent_40 = 0.40 * Sum
percent_50 = 0.50 * Sum
percent_60 = 0.60 * Sum
percent_70 = 0.70 * Sum
total = 0
count = 0
ticked_40 = 0
ticked_50 = 0
ticked_60 = 0
ticked_70 = 0
for x in np.nditer(s):
   total = total + x
   count = count + 1
   if total >= percent_40 and ticked_40 == 0:
      print (str(count) + ' makes up 40%')
      ticked_40 = 1
   elif total >= percent_50 and ticked_50 == 0:
      print (str(count) + ' makes up 50%')
      ticked_50 = 1
   elif total >= percent_60 and ticked_60 == 0:
      print (str(count) + ' makes up 60%')
      ticked_60 = 1
   elif total >= percent_70 and ticked_70 == 0:
      print (str(count) + ' makes up 70%')
      ticked_70 = 1
   else:
      pass
