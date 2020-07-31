from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxA = 0
        while left < right:
            maxA = max(maxA , min(height[left] , height[right]) * (right - left ) )
            if height[left] < height[right]:
                left +=1
            else:
                right -= 1
        return maxA



if __name__ == "__main__":
    height = [0,2]
    sol = Solution()
    total = sol.maxArea(height)
    print(total)
    