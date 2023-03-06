LINK: https://leetcode.com/problems/longest-substring-without-repeating-characters/

3. Longest substring without Repeating Characters

Description:

Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.


Idea: for this problem we will be using dicts. The intuition is that we will be saving each character into dict for each iteration. If we find the same element in the dict again we will be resetting the found element. We will be returing length of maximum substring.