'''
Understand - given the 2 strings, check if both contains the same # of characters regardless of order 
Match - 
Plan - 

    check the size of the 2 strings if not equal return false

    create a dict_s - key=char, value=occurance

    loop through s
        if dict_s has current char then increment its value
        if not add the character to dict_s with value 1

    create dict_t
    now loop through t
        check if current char is in dict_s
            check if the current char is in dict_t
                if so increment its value
                compare the chars valvue in the 2 dicts 
                if not same return False
        
        if not in dict_s return false

    return True at the end




'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        dict_s = {}

        for c in s:
            if c in dict_s:
                dict_s[c] += 1
            else:
                dict_s[c] = 1
            
        dict_t = {}

        for c in t:
            if c not in dict_s:
                return False
            else:
                if c in dict_t:
                    dict_t[c] += 1
                    if dict_t[c] > dict_s[c]:
                        return False
                else:
                    dict_t[c] = 1
        
        return True
        