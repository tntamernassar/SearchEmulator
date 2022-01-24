from Emulator.SearchAlgorithm import SearchAlgorithm
from Emulator.Graph import Node
import math


class DFS(SearchAlgorithm):
    def __init__(self):
        self.name = "DFS"
        self.open_list = None
        self.close_list = None

    def init_open(self):
        self.open_list = []
        self.close_list = []

    def h(self, v1: Node, v2: Node):
        x1, y1 = v1.name
        x2, y2 = v2.name
        return math.sqrt((y1-y2)**2 + (x1-x2)**2)

    def open(self, v: Node):
        self.open_list.append(v)

    def get_open_list(self) -> list:
        return self.open_list

    def get_open_size(self) -> int:
        return len(self.open_list)

    def close(self, v: Node):
        self.close_list.append(v)

    def get_close_list(self) -> list:
        return self.close_list

    def get_close_size(self):
        return len(self.close_list)

    def get_best(self) -> Node:
        n = self.open_list.pop()
        return n

    def is_closed(self, v: Node) -> bool:
        return v in self.close_list

    def is_opened(self, v: Node) -> bool:
        return v in self.open_list


class BFS(SearchAlgorithm):
    def __init__(self):
        self.name = "BFS"
        self.open_list = None
        self.close_list = None

    def init_open(self):
        self.open_list = []
        self.close_list = []

    def h(self, v1: Node, v2: Node):
        return 0

    def open(self, v: Node):
        self.open_list.append(v)

    def get_open_list(self) -> list:
        return self.open_list

    def get_open_size(self) -> int:
        return len(self.open_list)

    def close(self, v: Node):
        self.close_list.append(v)

    def get_close_list(self) -> list:
        return self.close_list

    def get_close_size(self):
        return len(self.close_list)

    def get_best(self) -> Node:
        n = self.open_list.pop(0)
        return n

    def is_closed(self, v: Node) -> bool:
        return v in self.close_list

    def is_opened(self, v: Node) -> bool:
        return v in self.open_list


class Heuristic(SearchAlgorithm):
    def __init__(self):
        self.name = "Heuristic"
        self.open_list = None
        self.close_list = None

    def init_open(self):
        self.open_list = []
        self.close_list = []

    def h(self, v1: Node, v2: Node):
        x1, y1 = v1.name
        x2, y2 = v2.name
        return math.sqrt((y1-y2)**2 + (x1-x2)**2)

    def open(self, v: Node):
        self.open_list.append(v)

    def get_open_list(self) -> list:
        return self.open_list

    def get_open_size(self) -> int:
        return len(self.open_list)

    def close(self, v: Node):
        self.close_list.append(v)

    def get_close_list(self) -> list:
        return self.close_list

    def get_close_size(self):
        return len(self.close_list)

    def get_best(self) -> Node:
        m = min(self.open_list, key=lambda node: node.h)
        self.open_list.remove(m)
        return m

    def is_closed(self, v: Node) -> bool:
        return v in self.close_list

    def is_opened(self, v: Node) -> bool:
        return v in self.open_list
