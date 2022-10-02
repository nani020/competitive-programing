class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        repeat, record = set(), set()
        for i in range(len(s)-9):
            substring = s[i:i+10]
            if substring in record:
                repeat.add(substring)
            else:
                record.add(substring)
        return list(repeat)