# Binary Sudoku Solver for Python

Author: Cody West
Update 1.0 (Last tested on 3 July 2019)
Requirements: 
	
	Python 3.6 or higher, MKAtoms, Clingo

Instructions:

	Unzip contents of file to a folder of your choosing (Note: you must have write permissions for
	this folder).
	Launch Binary.py using the command line (python3 /your/directory/Pinary.py).
	Input the puzzle you would like to solve.
	
Documentation:
	
	This python program attempts to solve a 6*6 Binary Sudoku Puzzle.
	The program uses tkinter for buiding the GUI and MKAtoms to make the GUI input into an atom
	for use in clingo. Clingo then follows the rules:
							1. Only 1 number may be stored in a cell
							2. Each row and column must have the same number of 1's and 0's
							3. Each row must be unique
							4. No number can appear in consecutive triples
	Once the system call for clingo has finished the answer set will be translated into the GUI
	for review by the user.
	
	Solve Button: Prepares the files needed for Clingo then calls Clingo using a system call.
	Clear Button: Emptys all cells on the board.
	Quit Button: Using destroy window quits the python program.
