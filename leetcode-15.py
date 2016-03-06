class Solution(object):
    # Time Limit Exceeded
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        print(nums)
        tmp = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp.append([nums[i], nums[j], nums[k]])
        return [list(q) for q in set(tuple(p) for p in tmp)]
