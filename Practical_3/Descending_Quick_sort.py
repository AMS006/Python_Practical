def Descending_partition(arr,beg,end):
    pivot = arr[end]
    i = beg-1
    j = beg
    while j<end:
        if arr[j]>pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
        j +=1
    
    arr[i+1],arr[end] = arr[end],arr[i+1]

    return i+1
def Descending_QuickSort(arr,beg,end):
    if beg<end:
        p = Descending_partition(arr,beg,end)
        Descending_QuickSort(arr,beg,p-1)
        Descending_QuickSort(arr,p+1,end)
arr = [3,6,1,8,4,2]
n = len(arr)
Descending_QuickSort(arr,0,n-1)
print(arr)