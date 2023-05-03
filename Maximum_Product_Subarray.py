# https://leetcode.com/problems/maximum-product-subarray/
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        ans = max(nums)
        curMin, curMax = 1,1 # 곱셈에 대한 중립값 1로 초기화

        for n in nums:
            tmp = curMax * n
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(tmp, curMin * n, n)
            ans = max(ans, curMax)
        return ans