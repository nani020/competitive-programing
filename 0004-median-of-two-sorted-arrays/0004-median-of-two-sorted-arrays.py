class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1+nums2
        a.sort()
        l = len(a)
        if(l%2):
            return a[(l-1)//2]/1 #Dividing by 1 to get the float value instead of an int
        else:
            return (a[l//2]+a[l//2-1])/2