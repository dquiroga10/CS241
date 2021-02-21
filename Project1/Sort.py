import time
import random

def selection_sort(arr):
    for i in range(len(arr)):
        old_val = arr[i]
        index = i
        low_val = old_val

        while index < len(arr):
            curr_val = arr[index]

            if curr_val <= low_val:
                low_val = curr_val
                low_vali = index
                index += 1

            else:
                index +=1

        arr[i] = low_val
        arr[low_vali] = old_val

def insertion_sort(arr):
    for i in range(1, len(arr)):
        curr_pos = arr[i]
        left_pos = arr[i-1]
        j = i

        while left_pos > curr_pos and j > 0:
            curr_pos = arr[j]
            left_pos = arr[j-1]

            if left_pos > curr_pos:
                arr[j] = left_pos
                arr [j-1] = curr_pos
                j -= 1
                

if __name__ == '__main__':
	arr1 = []
	arr2 = []
	arr3 = []
	arr4 = []
	arr5 = []
	arr6 = []
	for i in range(1000):
		arr1 += [i]
		arr2 += [i]
	for i in range(1000,0,-1):
		arr3 += [i]
		arr4 += [i]
	for i in range(1000):
		num = random.randint(0,1000)
		arr5 += [num]
		arr6 += [num]

	start = time.clock()
	selection_sort(arr1)
	end = time.clock()
	print('One Thousand Increasing Selection: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	selection_sort(arr3)
	end = time.clock()
	print('One Thousand Decreasing Selection: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	selection_sort(arr5)
	end = time.clock()
	print('One Thousand random Selection: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	insertion_sort(arr2)
	end = time.clock()
	print('One Thousand Increasing Insertion: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	insertion_sort(arr4)
	end = time.clock()
	print('One Thousand Decreasing Insertion: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	insertion_sort(arr6)
	end = time.clock()
	print('One Thousand random Insertion: ' + '{:.20f}'.format(end-start))

	arr7 = []
	arr8 = []
	arr9 = []
	arr10 = []
	arr11 = []
	arr12 = []
	for i in range(2500): 
		arr7 += [i]
		arr8 += [i]
	for i in range(2500,0,-1): 
		arr9 += [i]
		arr10 += [i]
	for i in range(2500): 
		num = random.randint(0,2500)
		arr11 += [num]
		arr12 += [num]

	start = time.clock()
	selection_sort(arr7)
	end = time.clock()
	print('Two Thousand, Five Hundred Increasing Selection: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	selection_sort(arr9)
	end = time.clock()
	print('Two Thousand, Five Hundred Decreasing Selection: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	selection_sort(arr11)
	end = time.clock()
	print('Two Thousand, Five Hundred random Selection: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	insertion_sort(arr8)
	end = time.clock()
	print('Two Thousand, Five Hundred Increasing Insertion: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	insertion_sort(arr10)
	end = time.clock()
	print('Two Thousand, Five Hundred Decreasing Insertion: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	insertion_sort(arr12)
	end = time.clock()
	print('Two Thousand, Five Hundred random Insertion: ' + '{:.20f}'.format(end-start))

	arr13 = []
	arr14 = []
	arr15 = []
	arr16 = []
	arr17 = []
	arr18 = []
	for i in range(5000): 
		arr13 += [i]
		arr14 += [i]
	for i in range(5000,0,-1): 
		arr15 += [i]
		arr16 += [i]
	for i in range(5000): 
		num = random.randint(0,5000)
		arr17 += [num]
		arr18 += [num]

	start = time.clock()
	selection_sort(arr13)
	end = time.clock()
	print('Five Thousand Increasing Selection: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	selection_sort(arr15)
	end = time.clock()
	print('Five Thousand Decreasing Selection: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	selection_sort(arr17)
	end = time.clock()
	print('Five Thousand random Selection: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	insertion_sort(arr14)
	end = time.clock()
	print('Five Thousand Increasing Insertion: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	insertion_sort(arr16)
	end = time.clock()
	print('Five Thousand Decreasing Insertion: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	insertion_sort(arr18)
	end = time.clock()
	print('Five Thousand random Insertion: ' + '{:.20f}'.format(end-start))

	arr19 = []
	arr20 = []
	arr21 = []
	arr22 = []
	arr23 = []
	arr24 = []
	for i in range(7500): 
		arr19 += [i]
		arr20 += [i]
	for i in range(7500,0,-1): 
		arr21 += [i]
		arr22 += [i]
	for i in range(7500): 
		num = random.randint(0,7500)
		arr23 += [num]
		arr24 += [num]

	start = time.clock()
	selection_sort(arr19)
	end = time.clock()
	print('Seven Thousand, Five Hundred Increasing Selection: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	selection_sort(arr21)
	end = time.clock()
	print('Seven Thousand, Five Hundred Decreasing Selection: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	selection_sort(arr23)
	end = time.clock()
	print('Seven Thousand, Five Hundred random Selection: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	insertion_sort(arr20)
	end = time.clock()
	print('Seven Thousand, Five Hundred Increasing Insertion: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	insertion_sort(arr22)
	end = time.clock()
	print('Seven Thousand, Five Hundred Decreasing Insertion: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	insertion_sort(arr24)
	end = time.clock()
	print('Seven Thousand, Five Hundred random Insertion: ' + '{:.20f}'.format(end-start))

	arr25 = []
	arr26 = []
	arr27 = []
	arr28 = []
	arr29 = []
	arr30 = []
	for i in range(10000): 
		arr25 += [i]
		arr26 += [i]
	for i in range(10000,0,-1): 
		arr27 += [i]
		arr28 += [i]
	for i in range(10000): 
		num = random.randint(0,10000)
		arr29 += [num]
		arr30 += [num]

	start = time.clock()
	selection_sort(arr25)
	end = time.clock()
	print('Ten Thousand Increasing Selection: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	selection_sort(arr27)
	end = time.clock()
	print('Ten Thousand Decreasing Selection: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	selection_sort(arr29)
	end = time.clock()
	print('Ten Thousand random Selection: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	insertion_sort(arr26)
	end = time.clock()
	print('Ten Thousand Increasing Insertion: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	insertion_sort(arr28)
	end = time.clock()
	print('Ten Thousand Decreasing Insertion: ' + '{:.20f}'.format(end-start))

	start = time.clock()
	insertion_sort(arr30)
	end = time.clock()
	print('Ten Thousand random Insertion: ' + '{:.20f}'.format(end-start))
