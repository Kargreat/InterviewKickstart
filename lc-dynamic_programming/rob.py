from typing import List

ip_ = [2,7,9,3,1]


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        else:
            robbed_amount = dict()
            # I have more than 2 elements
            robbed_amount[0] = nums[0]
            robbed_amount[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                robbed_amount[i] = nums[i] + robbed_amount[i-2] if nums[i] + robbed_amount[i-2] > robbed_amount[i-1] \
                    else robbed_amount[i-1]

        print(robbed_amount)
        return list(robbed_amount.values())[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.rob(nums=ip_))