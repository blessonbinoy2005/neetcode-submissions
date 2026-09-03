class Solution:
    '''
    FOR ORDERED ARRAY ONLY
    First 2 pointer tech
    create variable left = 0, right = len(nums) - 1
    create a loop left <= right
        total = nums[left] + nums[right]
        if total > target
            right--
        elif ntotal < target
            left++
        elif total == target
            return [left, right]

    return an empty tuple
    '''
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     left = 0
    #     right = len(nums) - 1

    #     while left <= right:
    #         total = nums[left] + nums[right]

    #         if total > target:
    #             right -= 1
    #         elif total < target:
    #             left += 1
    #         elif total == target:
    #             return [left, right]

    #     return [0,0]


    '''
    create a dict {}
    loop through nums with an index
        needed  = target - nums[i]
        if needed in dict
            return i,dict[needed]
        else:
            dict add nums[i], i

    return [0,0]

    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}

        for i in range(len(nums)):

            needed = target - nums[i] 

            if needed in dict:
                return [dict[needed], i]
            else:
                dict[nums[i]] = i
        
        return [0,0]



        