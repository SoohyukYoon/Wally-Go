import numpy as np  

# Rules to implement 
# 1 - prevent repetition 
# 2 - take all the stones if fully covered

class Game: 
	def __init__(self): 
		self.Board = np.zeros((19, 19))
		self.Prev_Board = np.zeros((19,19))

		self.Black = True

		self.Groups = {}

	def place(self, x, y): 
		if not (0 <= x < 19 and 0 <= y < 19): 
			return False
		if self.Black and self.legal_move(x, y) and self.check_capture(x, y): 
			self.Prev_Board[x][y] = self.Board[x][y]
			self.Board[x][y] = 1 
			self.Black = False
			print(f"Black Placed Stone at ({x}, {y})")
			return 
		elif not self.Black and self.legal_move(x, y and self.check_capture(x, y)): 
			self.Prev_Board[x][y] = self.Board[x][y]
			self.Board[x][y] = -1
			self.Black = True 
			print(f"White Placed Stone at ({x}, {y})")
			return 
		curr = "Black" if self.Black else "White"
		print(f"Illegal Move Made --- Move is still {curr}")
		return 
	
	def legal_move(self, x, y): 
		if self.Board[x][y] != 0: 
			return False 
		if self.Black and self.cannot_ko_take(x, y):
			return False
		if not self.Black and self.cannot_ko_take(x, y): 
			return False
		return True 
	

	def cannot_ko_take(self, x, y):
		# Corner case:  
		if (17 <= x <= 18 or 0 <= x <= 1) and (17 <= y <= 18 or 0 <= x <= 1): 
			grp_1 = 
			if self.Black: 

		# Side case: 

		# Inside case: 
		if self.Black:
			black_grp1 = self.Board[min(x + 2, 18)][y] + self.Board[min(x + 1, 18)][max(y - 1, 0)] + self.Board[min(x + 1, 18)][min(y + 1, 18)]
			black_grp2 = self.Board[max(x - 2, 0)][y] + self.Board[max(x - 1, 0)][max(y - 1, 0)] + self.Board[max(x - 1, 0)][min(y + 1, 18)]
			black_grp3 = self.Board[x][max(y - 2, 0)] + self.Board[min(x + 1, 18)][max(y - 1, 0)] + self.Board[max(x - 1, 0)][max(y - 1, 0)]
			black_grp4 = self.Board[x][min(y + 2, 18)] + self.Board[min(x + 1, 18)][min(y + 1, 18)] + self.Board[max(x - 1, 0)][min(y + 1, 18)]
			num_whites = self.Board[min(x + 1, 18)][y] + self.Board[x][min(y + 1, 18)] + self.Board[max(x - 1, 0)][y] + self.Board[x][max(y - 1, 0)]			
			is_ko = (num_whites == -4) and (black_grp1 == 3 or black_grp2 == 3 or black_grp3 == 3 or black_grp4 == 3)
			return is_ko and self.Prev_Board[x][y] == 1
		
		if not self.Black: 
			white_grp1 = self.Board[min(x + 2, 18)][y] + self.Board[min(x + 1, 18)][max(y - 1, 0)] + self.Board[min(x + 1, 18)][min(y + 1, 18)]
			white_grp2 = self.Board[max(x - 2, 0)][y] + self.Board[max(x - 1, 0)][max(y - 1, 0)] + self.Board[max(x - 1, 0)][min(y + 1, 18)]
			white_grp3 = self.Board[x][max(y - 2, 0)] + self.Board[min(x + 1, 18)][max(y - 1, 0)] + self.Board[max(x - 1, 0)][max(y - 1, 0)]
			white_grp4 = self.Board[x][min(y + 2, 18)] + self.Board[min(x + 1, 18)][min(y + 1, 18)] + self.Board[max(x - 1, 0)][min(y + 1, 18)]
			num_blacks = self.Board[min(x + 1, 18)][y] + self.Board[x][min(y + 1, 18)] + self.Board[max(x - 1, 0)][y] + self.Board[x][max(y - 1, 0)]
			is_ko = (num_blacks == 4) and (white_grp1 == -3 or white_grp2 == -3 or white_grp3 == -3 or white_grp4 == -3)
			return is_ko and self.Prev_Board[x][y] == -1

	def check_capture(self, x, y): 
		



	def get_board(self): 
		# Convert to black and white, np.where(condition, if_condition_true, if_condition_false)
		symbols = np.where(self.Board == 1, '●', np.where(self.Board == -1, '○', '.'))
		for row in symbols:
			# print space and the actual character
			print(' '.join(row))

def main(): 
	game = Game()

	while True: 
		try: 
			move = input("Enter a move x, y or 'quit' or 'print':")
			if move.lower() == 'quit':
				break

			if move.lower() == 'print': 
				game.get_board()

			x, y = map(int, move.split(','))
			game.place(x, y)
		except ValueError: 
			print("Did not put in valid values or formats")
		except KeyboardInterrupt: 
			break
if __name__ == "__main__": 
	main() 



		

		
	


