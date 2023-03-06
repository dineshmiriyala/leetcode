LINK: https://leetcode.com/problems/add-two-numbers/

ADD TWO NUMBERS:

Description:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
    2 ->4 ->3
    5 ->6 ->4
    ---------
    7 ->0 ->8

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Description: Here we will be using linked list data structure as our final output method. We will be performing addition operation on each node and saving it to nodes on final output node. We will be keeing track of carry as well the goal is to make a linked list with the sum of two numbers. from left to right. There is no real logic in this example but it teaches us how to handle linked lists.