def ways_toClimb(n):
    if n ==0:
        return 1
    if n<0:
        return 0
    
    return ways_toClimb(n-1)+ways_toClimb(n-2)+ways_toClimb(n-3)


print(ways_toClimb(5))