class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = int("".join([str(x) for x in digits]))
        digits += 1
        return list(str(digits))
        