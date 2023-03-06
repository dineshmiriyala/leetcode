#boiler plate code can be found in leetcode. link is in README.md

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums2) > len(nums1):
            temp = nums2
            nums2 = nums1
            nums1 = temp
        if len(nums2) == 0:
            if len(nums1) == 1:
                return float(nums1[0])
            elif len(nums1)%2 == 0:
                return(nums1[len(nums1)//2] + nums1[(len(nums1)//2) -1])/2.0
            else:
                return(nums1[len(nums1)//2])
        low = 0
        high = len(nums2)
        while low <= high:
            mid = (low + high) //2
            n1 = ((len(nums1) + len(nums2)) // 2) - mid
            l2 = self.getval(nums2, mid - 1)
            r2 = self.getval(nums2, mid)
            l1 = self.getval(nums1, n1 - 1)
            r1 = self.getval(nums1, n1)
            if l2 <= r1 and l1 <= r2 :
                if (len(nums2) + len(nums1)) %2 ==0:
                    return((max(l1,l2) + min(r1,r2)) /2.0)
                else:
                    return float(min(r1,r2))
            elif l1 >= r2:
                low = mid + 1
            else:
                high = mid - 1
    
    
    def getval(self, ar : List[int], i):
        if i < 0:
            return - sys.maxsize -1
        elif i == len(ar):
            return sys.maxsize + 1
        else:
            return ar[i]   