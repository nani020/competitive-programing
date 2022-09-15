class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums = [0] + nums

        prev = defaultdict(int)
    # prev[0] = 1

        total = 0

        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum - k in prev:
                total += prev[curr_sum - k]

            prev[curr_sum] += 1

        return total