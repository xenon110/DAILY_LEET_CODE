class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        INF = 10**20
        nums.sort()
        start = -INF
        count = 0
        for x in nums:
            if x - start > k:
                count= count + 1
                start = x
        return count