#boiler plate code can be found in leetcode.


class Solution(object):
   def lengthOfLongestSubstring(self, s):
      hook = 0
      pointer = 0
      d = {}
      ans = 0
      while (pointer < len(s)):
            if s[pointer] not in d:
                d[s[pointer]] = pointer
                pointer += 1
                ans = max(ans , len(d))
            else:
                del d[s[hook]]
                hook +=1
      return ans