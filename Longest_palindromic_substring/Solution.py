# boiler plate code can be found in leetcode.

class Solution:
    def longestPalindrome(self,s:str)-> str:
        self.lenmax = 0
        self.start = 0
        for i in range(len(s)):
            self.expandaroundcentre(s,i,i)
            self.expandaroundcentre(s,i,i+1)

        return s[self.start:self.start + self.lenmax]


    def expandaroundcentre(self,s:str, left:int, right:int)->int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left-=1
            right+=1

        if self.lenmax < right - left - 1:
            self.lenmax = right - left -1
            self.start = left + 1