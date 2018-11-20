def multiple():
	sum = 0
	for i in range(1,250):
		if i % 9 == 0:
			sum += i
		else:
		    continue
	return sum	    
	
sum = multiple()
print (sum)