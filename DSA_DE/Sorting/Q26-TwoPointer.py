def two_sum(nums,target):

    arr = [(nums[i],i) for i in range (len(nums))]
    arr.sort()

    left = 0
    right = len(arr)-1

    while(left<=right):

        current_sum = arr[left][0] + arr[right][0]


        if current_sum == target:
             return [arr[left][1], arr[right][1]]
        
        elif current_sum<target:
            left+=1
        else:
            right-=1

    return []        

print(two_sum([2,7,11,15],9))            

          

