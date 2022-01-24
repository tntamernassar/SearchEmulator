from Emulator.SearchEmulator import SearchEmulator
from SearchAlgorithms.SearchAlgorithms import DFS


SearchEmulator(gif_path='../gifs/maze.gif').emulate(image='../mazes/maze.png', algorithm=DFS())

