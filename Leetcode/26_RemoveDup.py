from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unq = {}
        for n in nums:
            if n not in unq:
                unq[n] =''
        return list(unq.keys())





if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    sol = Solution()
    length = sol.removeDuplicates(nums)
    print(length)
    