from typing import List

ip_ = [-2,1,-3,4,-1,2,1,-5,4]


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) > 0:
            cur_sum = max_sum = nums[0]
            for i in range(1, len(nums)):
                cur_sum = max(nums[i], cur_sum+nums[i])
                max_sum = max(max_sum, cur_sum)
            return max_sum
        return 0


if __name__ == '__main__':
    sol = Solution()


    print(sol.maxSubArray(ip_))