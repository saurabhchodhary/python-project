import random
A=int(input())
B=int(input())
d=random.randint(A,B+1)
print("randomaly picked number is %d"%(d))
if d%2==0:
    print("%d is an even number"%(d))
if d%2!=0:
    print("%d is an odd number"%(d))
if d>=0:
    print("%d is a positive number"%(d))
if d<0:
    print("%d is negative number"%(d))
if d==1:
   print("%d is neither prime NOR composite  number"%(d))
if d > 1:
	# Iterate from 2 to n / 2
	for i in range(2, int(d/2)+1):
		# If num is divisible by any number between
		# 2 and n / 2, it is not prime
		if (d % i) == 0:
			print(d, "is composite number")
			break
	else:
		print(d, "is a prime number")

'''f=open("knkl.txt","r")
f2=open("kh.txt","w")
for l in f:
	f2.write(l)
f2.close()'''
# Creating an output file in writing mode
'''output_file = open("knnnnnnkl.txt", "w")

# Opening input file and scanning each line
# from input file and writing in output file
with open("knkl.txt", "r") as scan:
	output_file.write(scan.read())

# Closing the output file
output_file.close()'''

'''l=["this is \n","python","programmiing"]
f=open("knkl.txt","w")
f.writelines(l)'''

l=['this is \n','hello','programming']
fin=open("C:/Users/saura/OneDrive/Documents/knkl.txt","a")
fin.writelines(l)
#for i in l:
 #   fin.write(i)




