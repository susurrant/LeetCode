"""
4. Median of Two Sorted Arrays
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        size = m + n
        median = 0
        i = 0
        j = 0
        if size % 2 == 0:
            idx0 = size//2-1
            idx1 = size//2
            while i < m or j < n:
                if i == m:
                    v = nums2[j]
                    j += 1
                elif j == n:
                    v = nums1[i]
                    i += 1
                elif nums1[i] < nums2[j]:
                    v = nums1[i]
                    i += 1
                else:
                    v = nums2[j]
                    j += 1

                if i + j - 1 == idx0:
                    median += v
                if i + j - 1 == idx1:
                    return (median+v)/2
        else:
            idx = (size - 1)//2
            while i < m or j < n:
                if i == m:
                    v = nums2[j]
                    j += 1
                elif j == n:
                    v = nums1[i]
                    i += 1
                elif nums1[i] < nums2[j]:
                    v = nums1[i]
                    i += 1
                else:
                    v = nums2[j]
                    j += 1

                if i + j - 1 == idx:
                    return v


if __name__ == '__main__':
    l1 = [1,3]
    l2 = [2]

    s = Solution()
    print(s.findMedianSortedArrays(l1, l2))