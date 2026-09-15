class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strs = ""
        whitespace = 0
        for char in s:
            if char.isspace():
                whitespace = 1
            else:
                if whitespace == 1:
                    strs = ""
                    whitespace = 0
                strs += char
        return len(strs)