import sys
def findMaxO(size,arr):
 max1 = -sys.maxsize
 max2 = -sys.maxsize
 min1 = sys.maxsize
 min2 = sys.maxsize

 for i in range(0,size):
    temp1 = arr[i]+i
    temp2 = arr[i]-i
    max1 = max(temp1,max1)
    max2 = max(temp2,max2)
    min1 = min(temp1,min1)
    min2 = min(temp1,min2)
    return max(max1-min1 , max2-min2)

 def findMaxB(size,ls):
    max = 0
    for i in range(0,size):
        for j in range(i+1,size):
            if(max<(abs(ls[i]-ls[j])+abs(i-j))):
                max = (abs(ls[i]-ls[j])+abs(i-j))
        return max

size = int(input('Enter the size of the array'))
ls =[]
for i in range(0,size):
    ls.append(int(input('Enter the elements')))

print(findMaxO(size,ls))