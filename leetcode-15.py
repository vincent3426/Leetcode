class Solution(object):
    # Time Limit Exceeded
    # O(n^3)
    # def threeSum(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     nums.sort()
    #     tmp = []
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             for k in range(j+1, len(nums)):
    #                 if nums[i] + nums[j] + nums[k] == 0:
    #                     tmp.append([nums[i], nums[j], nums[k]])
    #     return [list(q) for q in set(tuple(p) for p in tmp)]
    
    # O(nlogn)
    # 424ms 19.9%
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        tmp = []
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    tmp.append([nums[i], nums[j], nums[k]])
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return [list(q) for q in set(tuple(p) for p in tmp)]
