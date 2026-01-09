def isAnagram(s , t):
    dict = {}

    if (len(s) != len(t)):
        return False
    
    for letter in s:
        if(letter not in dict.keys()):
            dict[letter] = s.count(letter)
    print(dict)
     
    for letter in t:
        if(letter not in dict.keys()): 
            return False
        else:
            dict[letter] = dict.get(letter)-1
            if(dict.get(letter) == 0):
                dict.pop(letter)  

    if (len(dict)==0):
        return True
    else:
        False            
print(isAnagram("monalisa" , "lisamona" ))
