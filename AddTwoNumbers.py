class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		result = []
		c = 0
		while(l1 != None and l2 != None):
			result.append((l1.val+l2.val+c)%10)
			c = (l1.val+l2.val+c)/10
			l1 = l1.next
			l2 = l2.next
		while(l1 != None):
			result.append((l1.val+c)%10)
			c = (l1.val+c)/10
			l1 = l1.next
		while(l2 != None):
			result.append((l2.val+c)%10)
			c = (l2.val+c)/10
			l2 = l2.next
		if(c != 0):
			result.append(c)
		x = ListNode(result[0])
		temp = x
		for i in range(1, len(result)):
			node = ListNode(result[i])
			temp.next = node
			temp = temp.next
		return x

if __name__ == '__main__':
	for i in range(1, 10):
		print i

