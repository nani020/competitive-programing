class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagrams = []
        #Maintain a map of count of each character in p
        map = Counter(p)

        #How many distinct characters are in p
        distincts = len(map)

        i,j = 0,0

        #Window Size
        k = len(p)

        while(j < len(s)):
            # If current character is present in the map, decrement its count in map
            if s[j] in map:
                map[s[j]] -= 1
                #If its count is 0, decrement distincts
                if(map[s[j]] == 0): distincts -= 1
            if(j - i + 1 < k): j += 1
            else:
                #If number of distinct characters is 0 that means current window has all the required characters in required frequency so it is an anagram
                if(distincts == 0): anagrams.append(i)

                #Before incrementing i, check if ith character is there in map. If it is, then increment its count
                if s[i] in map: 
                    map[s[i]] += 1
                    #And if the count is 1 then increment distincts
                    if(map[s[i]] == 1): distincts += 1
                #Slide the window to right
                i += 1
                j += 1

        return anagrams
        