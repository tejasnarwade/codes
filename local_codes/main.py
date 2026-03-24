def bubble(arr:list[int])-> list[int]:
	n = len(arr)
	for i in range(n-1):
		if arr[i]>arr[i+1]:
			arr[i],arr[i+1]=arr[i+1],arr[i]
		else:
			pass
	return arr

print(bubble([2,1,4,5]))
