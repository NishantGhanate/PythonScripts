from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,n in enumerate(nums):
            temp = target - n 
            if temp in dic:
                return [dic[temp] , i]
            dic[n] = i
        return []

if __name__ == "__main__":
    target = 9
    nums = [1,2,4,6,7]
    sol = Solution()
    indexs = sol.twoSum(nums, target)
    print(indexs)
    
