import statistics 

def totsum (s):
 tot=0
 for indic in range(len(s)):
  tot = tot + s[indic]
 return tot
  	
def average (s):
 aver = total/10
 return aver
def standevia (s):
	sd = statistics.stdev(li)
	return sd
li = []
cont=0

while (cont<10):
 cont = cont+1
 n = float(input("Give me a number: "))
 li.append(n)
 total = totsum(li)
 avera = average(li)
devi = standevia(li)
print ("no more values")
print (" the sum is: ",total)
print ("the average is: ",avera)
print ("the standard deviation is: ",devi)	