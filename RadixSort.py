import numpy as np

#exec(open("[location]//[file].py").read()) #python3

#get digit of the number
def fn_GetIndex(arr_args):
	# index(0): Number / index(1) digit
	return int( (arr_args[0]% pow(10,arr_args[1]))/ (pow(10,arr_args)/10))

#radix sort known sorting algorithm for sorting with no comparisons only using arrays
def fn_RadixSort(int_arr):
	MaxDigits = len(str(max(int_arr))) #number of digits in the max number in array
	n=MaxDigits
	i=0
	Storage=[[] for ar in range(10) ]

	#max itteration to the max number of digits of the max number
	for x in xrange(1,n):
		#categorize each number to its array
		while i < len(int_arr):
			index = fn_GetIndex([int_arr[i],x])
			Storage[index].append(int_arr[i])
			i=i+1
		#re-initialize for itteration
		int_arr = np.concatenate(Storage).tolist() #flatten the double array into 1 single array
		print(int_arr) # display Changes of each itteration
		Storage=[[] for ar in range(10)]
		i=0
	return int_arr


