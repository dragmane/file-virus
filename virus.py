import random
import string
letters = string. ascii_letters
d = input("file name or path to corrupt : ")
outF = open(d, "w" )
for i in range(500):
 
   r = ' ' . join(random .choice(letters) for i in range(500))
print(r)
 


for line in r:
# write line to output file
  outF.write(line)
  outF.write("/n")
outF.close()
