class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		length = len(nums1) + len(nums2)
		if length % 2 == 0:
			return (self.findKth(nums1, nums2, length/2)+self.findKth(nums1, nums2, length/2-1))/2.0
		else:
			return self.findKth(nums1, nums2, length/2)


	def findKth(self, nums1, nums2, k):
		if not nums1:
			return nums2[k]
		if not nums2:
			return nums1[k]
		if k == 0:
			return min(nums1[0], nums2[0])
		length1 = len(nums1)
		length2 = len(nums2)
		if nums1[length1/2] > nums2[length2/2]:
			if k > length1/2+length2/2:
				return self.findKth(nums1, nums2[length2/2+1:], k-length2/2-1)
			else:
				return self.findKth(nums1[:length1/2], nums2, k)
		else:
			if k > length1/2+length2/2:
				return self.findKth(nums1[length1/2+1:], nums2, k-length1/2-1)
			else:
				return self.findKth(nums1, nums2[:length2/2], k)



if __name__ == '__main__':
	solu = Solution()
	nums1 = [1, 2]
	nums2 = [3, 4]
	x = solu.findMedianSortedArrays(nums1, nums2)
	print x