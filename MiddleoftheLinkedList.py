class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def middleNode(self, head):
		length = 0;
		temp = head
		while temp != None:
			temp = temp.next
			length += 1
		length //= 2
		print(length)
		temp = head
		while length > 0:
			temp = temp.next
			length -= 1
		return 

if __name__ == '__main__':
	print(5//2)