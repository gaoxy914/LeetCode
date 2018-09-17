class Solution(object):
	def countBattleships(self, board):
		count = 0
		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] == 'X':
					flag = True
					if i-1 >= 0 and board[i-1][j] == 'X':
						flag = False
					if j-1 >= 0 and board[i][j-1] == 'X':
						flag = False
					if flag:
						count += 1
		return count