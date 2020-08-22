from typing import List

ip_ = [2,7,3,6]
total = 9


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        if len(nums) >= 2:
            indices = {}
            for i in range(0, len(nums)):
                if target - nums[i] in indices:
                    return [indices[target-nums[i]], i]
                else:
                    indices[nums[i]] = i

        return []


if __name__ == '__main__':
    print(Solution.twoSum(ip_, total))