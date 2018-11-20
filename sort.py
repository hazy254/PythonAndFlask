def list_sort(list1):
	list2 = []
	for i in list1:
		if len(list2) == 0:
			list2.insert(0, i)
			print (list2)
		else:
			for x in range(0, len(list2)):
				if len(list2[x]) > len(i):
					list2.insert(x, i)
				elif len(list2[x]) == len(i):
					continue
				else:
					list2.append(i)
	return list2
a = ["cow", "pigs", "teachers", "steven", "me"]
dog = list_sort(a)
print (dog)