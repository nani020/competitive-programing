class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		l=1
		for s in range(1,len(nums)):
			if nums[s]!=nums[s-1]:
				nums[l]=nums[s]
				l += 1
		return l