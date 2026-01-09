def swap(arr , pos1 , pos2):
    arr[pos1],arr[pos2] = arr[pos2],arr[pos1]


def partition(arr , low , high , pivot):
    i = low
    j = low

    while i < high:
        if arr[i]>pivot:
            i+=1
        else:
            swap(arr,i,j)
            i+=1
            j+=1    
    return j-1   


def QuickSort(arr , low , high):
    if low<high:
        pivot = arr[high]
        pos = partition(arr , low , high , pivot)

        QuickSort(arr,low,pos-1)
        QuickSort(arr,pos+1,high)


arr = [20,10,40,30,90,80]   
QuickSort(arr, 0, len(arr) - 1)
print("Sorted Array",arr)    