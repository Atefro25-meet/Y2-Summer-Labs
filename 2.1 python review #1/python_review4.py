import random
daysofweek=["sunday","monday","tuseday","wednesday","thursday","friday","saturday"]
evens=0


temp=[]
for i in range(7) :
	temp.append(random.randint(26,41))

print

for i in range(7):
	if temp[i]%2==0:
		evens=evens+1  #maybe here
print("good days count:"+ str(evens))

for x in range(0,7):
	print(daysofweek[x],":",temp[x])




highestemp= 26
highestempday='sunday'

for i in range(7):
	if temp[i]>highestemp:
		highestemp=temp[i]
		highestempday=daysofweek[i]
print("highestemp:"+str(highestempday)+":"+str(highestemp))


lowestemp=40
lowestempday='sunday'

for i in range(7):
	if temp[i]<lowestemp:
		lowestemp=temp[i]
		lowestempday=daysofweek[i]
print("lowestemp:"+str(lowestempday)+":"+str(lowestemp))

sumotemps=0
for i in range(7):
	sumotemps += temp[i]

avg=sumotemps/7
print("avg:"+str(avg))
aboveavg=[]

for i in range(7):
	if temp[i]>avg:
		aboveavg.append(daysofweek[i])
print("above avg days:"+str(aboveavg))
