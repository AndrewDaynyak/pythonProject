def quick_sort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=arr[0]
        less=[i for i in arr[1:] if i<pivot]
        greater=[i for i in arr[1:] if i>pivot]
        return quick_sort(less)+[pivot]+quick_sort(greater)

x=quick_sort([100,90,76,55,34,32,28,24,18,14,9])
print(x)

