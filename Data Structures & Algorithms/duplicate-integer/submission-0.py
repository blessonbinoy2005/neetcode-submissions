'''
Understand - Check if any values appear more than once in nums
Match - We can use HashSet
Plan - 
    Create an HashSet
    create a for loop that loops through nums
    if x is in hashset return false
    else
    add x to hashset
    outside the loop return true
Edge case - 
    if nums is empty return true

'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        my_set = set()

        if not nums:
            return False


        for x in nums:
            if x in my_set:
                return True
            else:
                my_set.add(x)
        
        return False

        