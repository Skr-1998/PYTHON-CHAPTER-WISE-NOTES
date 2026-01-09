

def isValid(s):
    dict_parenthisis = {
        '(':')',
        '{':'}',
        '[':']',
    }

    if(len(s) == 1):
        return False
    i = 0
    stack = []

    while(i<len(s)):
        if(s[i]=='(' or s[i]=='{' or s[i]=='['):
            stack.insert(0,s[i])
        else:
            if(len(stack)>0):
                top=stack.pop(0)
                if(dict_parenthisis[top]!=s[i]):
                    return False
            elif(len(stack)==0):
                return False
            
        i+=1
        if(len(stack)>0):
            return False
    return True        




