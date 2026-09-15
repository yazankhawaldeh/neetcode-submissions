class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # workflow:
        # 1. take word in list
        # 2. for each char, comp to ascii (a) and that number is where 1 is incremented
        # 3. this array serves as the key for hashmap: we parse to tuple since immutable and assign the current
        # word (value) to this key.
        # if another string comes along, we compare its tuple to the hashes we already made then append
        # rinse and repeat
        stringMap = {}
        for i in range (len(strs)):
            charArray = [0] * 26 # alphabet!
            for char in strs[i]:
                charArray[ord(char)-ord('a')] += 1
            t = tuple(charArray)
            if t not in stringMap.keys():
                stringMap[t] = []
                stringMap[t].append(strs[i])
            elif t in stringMap.keys():
                stringMap[t].append(strs[i])
            

        last = list(stringMap.values())
        return last
        