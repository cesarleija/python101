import collections

def isWordPalindrome(uword):
    sword = ""
    if len(uword) > 0: 
        sword = uword
    else:
        return False

    return list(sword) == list(reversed(sword))
    

