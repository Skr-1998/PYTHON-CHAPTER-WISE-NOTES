def similarPair(word):
    count = 0

    for i in range(0, len(word)-1):
        dict_i = {}
        for character in word[i]:
            if(character not in dict_i):
                dict_i[character] = 1

        for j in range(i+1, len(word)):
            dict_j = {}
            for character in word[j]:
              if(character not in dict_j.keys()):
                dict_j[character] = 1 
            if ( dict_i == dict_j):
               count+=1

    return count               



print(similarPair(["aba","aabb","abcd","bac","aabc"])) 
