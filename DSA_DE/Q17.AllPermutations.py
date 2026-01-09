#[1,2,3] - [F,F,F]

def allPermutations(arr,flags,ans,n):
    
    if(all(flags) == True):
        print(ans)
        return
    for i in range(0,n):
        if(flags[i] == False):
          flags[i]= True
          ans.append(arr[i])
          allPermutations(arr,flags,ans,n)
          flags[i]= False
          ans.pop()



allPermutations([1,2,3],[False,False,False],[],3)