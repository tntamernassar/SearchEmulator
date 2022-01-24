from Emulator.SearchEmulator import SearchEmulator
from SearchAlgorithms.SearchAlgorithms import BFS


SearchEmulator(gif_path='../gifs/maze.gif').emulate('../mazes/maze.png', BFS())

