from __future__ import print_function
def eprint(*args, **kwargs): print(*args, file=sys.stderr, **kwargs)
from pickle import NONE
from xxlimited import Xxo
import numpy as np
import sys
import random 
VERSION = '1.0'

# GO Boards
board_9x9 = [
	7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
	7, 1, 0, 2, 0, 0, 0, 0, 1, 2, 7,
	7, 1, 1, 2, 0, 0, 0, 0, 1, 2, 7,
	7, 2, 2, 0, 0, 0, 0, 1, 2, 2, 7,
	7, 0, 0, 1, 1, 0, 1, 0, 1, 0, 7,
	7, 0, 0, 1, 2, 2, 2, 1, 0, 0, 7,
	7, 0, 0, 1, 1, 2, 1, 0, 0, 0, 7,
	7, 0, 0, 0, 1, 2, 2, 1, 0, 0, 7,
	7, 0, 0, 0, 0, 1, 1, 0, 0, 0, 7,
	7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]

# 9x9 coordinates: 
coords_9x9 = [
	'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 
	'XX', 'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'J9', 'XX', 
	'XX', 'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'J8', 'XX', 
	'XX', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'J7', 'XX', 
	'XX', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'J6', 'XX', 
	'XX', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'J5', 'XX', 
	'XX', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'J4', 'XX', 
	'XX', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'J3', 'XX', 
	'XX', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'J2', 'XX', 
	'XX', 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'J1', 'XX', 
	'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'
]

board_13x13 = [
	7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
	7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 1, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 8, 1, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 0, 8, 2, 8, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 0, 0, 8, 0, 6, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]

# 13x13 coordinates
coords_13x13 = [
    'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',
    'XX',  'A13', 'B13', 'C13', 'D13', 'E13', 'F13', 'G13', 'H13', 'J13', 'K13', 'L13', 'M13', 'N13', 'XX',
    'XX',  'A12', 'B12', 'C12', 'D12', 'E12', 'F12', 'G12', 'H12', 'J12', 'K12', 'L12', 'M12', 'N12', 'XX',
    'XX',  'A11', 'B11', 'C11', 'D11', 'E11', 'F11', 'G11', 'H11', 'J11', 'K11', 'L11', 'M11', 'N11', 'XX',
    'XX',  'A10', 'B10', 'C10', 'D10', 'E10', 'F10', 'G10', 'H10', 'J10', 'K10', 'L10', 'M10', 'N10', 'XX',
    'XX',  'A9',  'B9',  'C9',  'D9',  'E9',  'F9',  'G9',  'H9',  'J9',  'K9',  'L9',  'M9',  'N9',  'XX',
    'XX',  'A8',  'B8',  'C8',  'D8',  'E8',  'F8',  'G8',  'H8',  'J8',  'K8',  'L8',  'M8',  'N8',  'XX',
    'XX',  'A7',  'B7',  'C7',  'D7',  'E7',  'F7',  'G7',  'H7',  'J7',  'K7',  'L7',  'M7',  'N7',  'XX',
    'XX',  'A6',  'B6',  'C6',  'D6',  'E6',  'F6',  'G6',  'H6',  'J6',  'K6',  'L6',  'M6',  'N6',  'XX',
    'XX',  'A5',  'B5',  'C5',  'D5',  'E5',  'F5',  'G5',  'H5',  'J5',  'K5',  'L5',  'M5',  'N5',  'XX',
    'XX',  'A4',  'B4',  'C4',  'D4',  'E4',  'F4',  'G4',  'H4',  'J4',  'K4',  'L4',  'M4',  'N4',  'XX',
    'XX',  'A3',  'B3',  'C3',  'D3',  'E3',  'F3',  'G3',  'H3',  'J3',  'K3',  'L3',  'M3',  'N3',  'XX',
    'XX',  'A2',  'B2',  'C2',  'D2',  'E2',  'F2',  'G2',  'H2',  'J2',  'K2',  'L2',  'M2',  'N2',  'XX',
    'XX',  'A1',  'B1',  'C1',  'D1',  'E1',  'F1',  'G1',  'H1',  'J1',  'K1',  'L1',  'M1',  'N1',  'XX',
    'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX'
]

board_19x19 = [
	7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
	7, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 7,
	7, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
	7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]

# 19x19 coordiantes
coords_19x19 = [
    'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',
    'XX',  'A19', 'B19', 'C19', 'D19', 'E19', 'F19', 'G19', 'H19', 'J19', 'K19', 'L19', 'M19', 'N19', 'O19', 'P19', 'Q19', 'R19', 'S19', 'T19', 'XX',
    'XX',  'A18', 'B18', 'C18', 'D18', 'E18', 'F18', 'G18', 'H18', 'J18', 'K18', 'L18', 'M18', 'N18', 'O18', 'P18', 'Q18', 'R18', 'S18', 'T18', 'XX',
    'XX',  'A17', 'B17', 'C17', 'D17', 'E17', 'F17', 'G17', 'H17', 'J17', 'K17', 'L17', 'M17', 'N17', 'O17', 'P17', 'Q17', 'R17', 'S17', 'T17', 'XX',
    'XX',  'A16', 'B16', 'C16', 'D16', 'E16', 'F16', 'G16', 'H16', 'J16', 'K16', 'L16', 'M16', 'N16', 'O16', 'P16', 'Q16', 'R16', 'S16', 'T16', 'XX',
    'XX',  'A15', 'B15', 'C15', 'D15', 'E15', 'F15', 'G15', 'H15', 'J15', 'K15', 'L15', 'M15', 'N15', 'O15', 'P15', 'Q15', 'R15', 'S15', 'T15', 'XX',
    'XX',  'A14', 'B14', 'C14', 'D14', 'E14', 'F14', 'G14', 'H14', 'J14', 'K14', 'L14', 'M14', 'N14', 'O14', 'P14', 'Q14', 'R14', 'S14', 'T14', 'XX',
    'XX',  'A13', 'B13', 'C13', 'D13', 'E13', 'F13', 'G13', 'H13', 'J13', 'K13', 'L13', 'M13', 'N13', 'O13', 'P13', 'Q13', 'R13', 'S13', 'T13', 'XX',
    'XX',  'A12', 'B12', 'C12', 'D12', 'E12', 'F12', 'G12', 'H12', 'J12', 'K12', 'L12', 'M12', 'N12', 'O12', 'P12', 'Q12', 'R12', 'S12', 'T12', 'XX',
    'XX',  'A11', 'B11', 'C11', 'D11', 'E11', 'F11', 'G11', 'H11', 'J11', 'K11', 'L11', 'M11', 'N11', 'O11', 'P11', 'Q11', 'R11', 'S11', 'T11', 'XX',
    'XX',  'A10', 'B10', 'C10', 'D10', 'E10', 'F10', 'G10', 'H10', 'J10', 'K10', 'L10', 'M10', 'N10', 'O10', 'P10', 'Q10', 'R10', 'S10', 'T10', 'XX',
    'XX',  'A9',  'B9',  'C9',  'D9',  'E9',  'F9',  'G9',  'H9',  'J9',  'K9',  'L9',  'M9',  'N9',  'O9',  'P9',  'Q9',  'R9',  'S9',  'T9',  'XX',
    'XX',  'A8',  'B8',  'C8',  'D8',  'E8',  'F8',  'G8',  'H8',  'J8',  'K8',  'L8',  'M8',  'N8',  'O8',  'P8',  'Q8',  'R8',  'S8',  'T8',  'XX',
    'XX',  'A7',  'B7',  'C7',  'D7',  'E7',  'F7',  'G7',  'H7',  'J7',  'K7',  'L7',  'M7',  'N7',  'O7',  'P7',  'Q7',  'R7',  'S7',  'T7',  'XX',
    'XX',  'A6',  'B6',  'C6',  'D6',  'E6',  'F6',  'G6',  'H6',  'J6',  'K6',  'L6',  'M6',  'N6',  'O6',  'P6',  'Q6',  'R6',  'S6',  'T6',  'XX',
    'XX',  'A5',  'B5',  'C5',  'D5',  'E5',  'F5',  'G5',  'H5',  'J5',  'K5',  'L5',  'M5',  'N5',  'O5',  'P5',  'Q5',  'R5',  'S5',  'T5',  'XX',
    'XX',  'A4',  'B4',  'C4',  'D4',  'E4',  'F4',  'G4',  'H4',  'J4',  'K4',  'L4',  'M4',  'N4',  'O4',  'P4',  'Q4',  'R4',  'S4',  'T4',  'XX',
    'XX',  'A3',  'B3',  'C3',  'D3',  'E3',  'F3',  'G3',  'H3',  'J3',  'K3',  'L3',  'M3',  'N3',  'O3',  'P3',  'Q3',  'R3',  'S3',  'T3',  'XX',
    'XX',  'A2',  'B2',  'C2',  'D2',  'E2',  'F2',  'G2',  'H2',  'J2',  'K2',  'L2',  'M2',  'N2',  'O2',  'P2',  'Q2',  'R2',  'S2',  'T2',  'XX',
    'XX',  'A1',  'B1',  'C1',  'D1',  'E1',  'F1',  'G1',  'H1',  'J1',  'K1',  'L1',  'M1',  'N1',  'O1',  'P1',  'Q1',  'R1',  'S1',  'T1',  'XX',
    'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX',  'XX'
]

# Boards lookup, for initialization purposes 
BOARDS = {
	'9' : board_9x9, 
	'13': board_13x13, 
	'19': board_19x19
}

# Coords look up, for initialization purposes
COORDS = {
	'9' : coords_9x9, 
	'13': coords_13x13, 
	'19': coords_19x19
}


# Board select
BOARD = None
COORD = None

BOARD_WIDTH = 0
BOARD_RANGE = 0
MARGIN = 2 
files = "     a b c d e f g h j k l m n o p q r s t"

# count 
liberties = [] 
block = []


# ASCII Char for pieces
EMPTY = 0
BLACK = 1 
WHITE = 2 
MARKER = 4 
OFFBOARD = 7 
LIBERTY = 8 

#ASCII rep of stones 
pieces = '.●○  bw +'


def print_board(): 
	# loop over board rows. 
	for row in range(1, BOARD_RANGE): 
		# loop over board columns: 
		if BOARD_RANGE != 11 and row < BOARD_RANGE - 1:
			print(f'  {BOARD_WIDTH + 1 - row:2d}', end='')  
		elif row < BOARD_RANGE - 1:
			print(f' {BOARD_WIDTH + 1 - row:2d}', end='')

		for col in range(BOARD_RANGE): 
			square = row * BOARD_RANGE  + col
			# init stone 
			stone = BOARD[square]
			if stone != ' ': print(pieces[stone], end=' ')
		print()
	print(" ", files[1:BOARD_RANGE * 2])

def set_board_size(command): 	
	global BOARD_WIDTH, BOARD_RANGE, MARGIN, BOARD, COORD
	# parse the board size
	size = int(command.split()[-1])

	# throw error if board size is not supported
	if size not in [9, 13, 19]: 
		print('? not supported board size\n')
		return 
		
	# otherwise set board size
	BOARD_WIDTH = size 
	BOARD_RANGE = BOARD_WIDTH + MARGIN
	BOARD = BOARDS[str(size)]
	COORD = COORDS[str(size)]

# count liberties, save stone group coords 
# Implementation note: Has one issue, if we chose a spot that does not 
# have a stone, but a stone is next to it then it will falsely mark itself 
# as marked with "+".
def count(square, color): 
	# init piece
	piece = BOARD[square]
	# skip offboard square
	if piece == OFFBOARD: return 		

	# if there is a stone at square 
	if piece and piece & color and (piece & MARKER) == 0:
		# save stone's coordinate 
		block.append(square)

		# mark the stone ## Why we do this? ## 
		BOARD[square] |= MARKER 

		# look for neighbours recursively 
		count(square + BOARD_RANGE, color)	# NORTH
		count(square - BOARD_RANGE, color)  # SOUTH
		count(square + 1, color)			# EAST
		count(square - 1, color)			# WEST
	
	# if square is empty
	elif piece == EMPTY:
		BOARD[square] |= LIBERTY 
		liberties.append(square)

# remove captured stones
def clear_block(): 
	for captured in block: BOARD[captured] = EMPTY

# clears the liberties and block
def clear_group(): 
	global block, liberties 

	# clear block and liberties lists
	block = []
	liberties = []

# restor the board aftrer counting stones
def restore_board(): 
	clear_group()

	# unmark stones 
	for square in range(BOARD_RANGE ** 2): 
		# if the square is on board
		if BOARD[square] != OFFBOARD: 
			# restore piece 
			# i.e. 0110 --- marked black stone
			# 	   0011 --- 0s the marked stone
			#    &_____
			#      0010
			BOARD[square] &= 3
			
# clear the entire board --- make empty 
def clear_board(): 
	clear_group()
	for square in range(len(BOARD)): 
		if BOARD[square] != OFFBOARD: 
			BOARD[square] = EMPTY

# handle captures
def captures(color): 
	# loop over the board square
	for square in range(len(BOARD)): 
		# init piece
		piece = BOARD[square]

		# skip offboard square
		if piece == OFFBOARD: continue 

		# if stone belongs to the given color 
		if piece & color: 
			# count liberties
			count(square, color)

			# if no liberties left remove the stones 
			if len(liberties) == 0: clear_block()

			# restore the board
			restore_board()

# sets the stone
def set_stone(square, color): 
	# make move on board
	BOARD[square] = color

	# handle capture of opp color, bc 3 - WHITE = BLACK and 3 - BLACK = WHITE
	captures(3 - color)

# generate random move 
def make_random_move(color): 
	# generate empty random square
	random_square = random.randrange(len(BOARD))
	
	while BOARD[random_square] != EMPTY:
		random_square = random.randrange(len(BOARD))
			
	set_stone(random_square, color)

	count(random_square, color)

	if len(liberties) == 0: 

		restore_board()

		BOARD[random_square] = EMPTY

		try: 
			# return suicide move
			return make_random_move(color)
		except:
			# make pass move 
			return ''
	
	restore_board()

	# return the move 
	return COORD[random_square]

# play command 
def play(command):
	# parse color
	color = BLACK if command.split()[1] == 'B' else WHITE

	# parse square 
	square_str = command.split()[-1]
	if square_str[1:5] == "pass": 
		return ''

	# ord converts ASCII to nu: A is smallest alphabet value, +1 to make it 1-indexed
	col = ord(square_str[0]) - ord('A') + 1 if ord(square_str[0]) < ord('I') else ord(square_str[0]) - ord('A')
	row = (BOARD_RANGE - 1) - int(square_str[1:])
	square = row * BOARD_RANGE + col

	set_stone(square, color)

# edge detection 
def detect_edge(square): 
	# loop over 4 directions 
	for direction in [BOARD_RANGE, 1, -BOARD_RANGE, -1]: 
		# it is board edge
		if BOARD[square + direction] == OFFBOARD: return True
	# not board edge
	return False

# evalute best liberty to extend/surround
def evaluate(color): 
	# max number of liberties found 
	best_count = 0 
	possible_liberties = list(liberties)
	if not possible_liberties: 
		return None
	best_liberty = possible_liberties[0]
	# loop over the liberties within the list
	for liberty in possible_liberties: 
		# restore for empty liberties list
		restore_board()

		# put stone on board 
		BOARD[liberty] = color

		# count new liberties 
		count(liberty, color)

		# found more liberties 
		if len(liberties) > best_count and not detect_edge(liberty): 
			best_liberty = liberty 
			best_count = len(liberties)

		# restore for last iteration
		restore_board()

		# remove stone off board 
		BOARD[liberty] = EMPTY

	# return best liberty 
	return best_liberty 


# generate move
def genmove(color): 

	best_move = 0 
	capture = 0 
	save = 0 
	defend = 0 
	surround = 0 

	# capture opponent's group 
	for square in range(len(BOARD)): 
		# init piece
		piece = BOARD[square]

		# match opponent's group 
		if piece & (3 - color): 
			# count liberties for opponent's group 
			count(square, 3 - color)

			# if 1 liberty left, capture
			if len(liberties) == 1: 
				# save the capture move 
				target_square = liberties[0]
				best_move = target_square 
				capture = target_square
				break 
		
			# restore board
			restore_board()

	# save own group 
	for square in range(len(BOARD)): 
		# init piece
		piece = BOARD[square]

		# match own group 
		if piece & color: 
			# count liberties for opponent's group 
			count(square, color)

			# if 1 liberty left, capture
			if len(liberties) == 1: 

				# save the capture move 
				target_square = liberties[0]
				best_move_prev = best_move
				best_move = target_square 
				save = target_square

				# check if saving makes no change
				set_stone(target_square, color)
				count(target_square, color)
				if len(liberties) == 1 or len(liberties) == 0: best_move = best_move_prev
				BOARD[target_square] = EMPTY
				break 
			# restore board
			restore_board()

	# defend own group
	for square in range(len(BOARD)): 
		# init piece
		piece = BOARD[square]

		# match own group 
		if piece & color: 
			# count liberties for opponent's group 
			count(square, color)

			# if 1 liberty left, capture
			if len(liberties) == 2: 

				# save the capture move 
				best_liberty = evaluate(color)
				best_move = best_liberty 
				save = best_liberty 
				break 

			# restore board
			restore_board()

	# surround opponent's group 
	for square in range(len(BOARD)): 
		# init piece
		piece = BOARD[square]

		# match opponent's group 
		if piece & (3 - color): 
			# count liberties for opponent's group 
			count(square, 3 - color)

			# if group has two liberties
			if len(liberties) > 1: 

				# save the capture move 
				best_liberty = evaluate(color)
				best_move = best_liberty 
				surround = best_liberty 
				break 

			# restore board
			restore_board()

	if best_move: 
		# print available moves 
		eprint('capture move', COORD[capture])
		eprint('save move:', COORD[save])
		eprint('defend move:', COORD[defend])
		eprint('surround move:', COORD[surround])
		
		# handle AI move priorities
		if not capture and not defend and not save: best_move = surround
		if not capture and not save and defend: best_move = defend
		if not capture and not defend and save: best_move = save
		if capture: best_move = capture
		
		# make BEST move
		set_stone(best_move, color)

		# check if suicide move 
		count(best_move, color)

		# check if suicide move
		# diff way to do compared to make_random_move
		legal = len(liberties)
		
		restore_board()

		if not legal: 
			# remove stone from board: 
			BOARD[best_move] = EMPTY
			eprint('avoided suicide move, making rand instead')

			# consider random move instead
			return make_random_move(color)
		
		eprint('best move', COORD[best_move])
		return COORD[best_move]

	# eprint('random move')
	return make_random_move(color)


# GTP communication protocol  
def gtp(): 
	# main GTP loop 
	while True: 
		#accept GUI command
		command = input()

		# handle command 
		if 'name' in command: print('= Wally\n')
		elif 'protocol_version' in command: print('= 1\n')
		elif 'version' in command: print('=', VERSION, '\n')
		elif 'list_commands' in command: print('= protocol_version\n')
		elif 'boardsize' in command: set_board_size(command); print('=\n')
		elif 'clear_board' in command: clear_board(); print('=\n')
		elif 'showboard' in command: print('='); print_board(); print()
		elif 'play' in command: play(command); print('=\n')
		elif 'genmove' in command: print('=', genmove(BLACK if command.split()[-1] == 'B' else WHITE) + '\n')
		elif 'quit' in command: sys.exit() 
		else: print('=\n') # skip current unsupported commands 

# start gpt communication 
gtp()


set_board_size('boardsize 9')
print_board()
play('play B B9')
captures(BLACK)
print_board()
