from Emulator.Graph import Graph, Node
import time


class SearchAlgorithm:
    def __init__(self, name):
        self.name = name

    def init_open(self):
        pass

    def h(self, v1: Node, v2: Node):
        return 0

    def open(self, v: Node):
        pass

    def get_open_list(self) -> list:
        pass

    def get_open_size(self) -> int:
        pass

    def close(self, v: Node):
        pass

    def get_close_list(self) -> list:
        pass

    def get_close_size(self):
        pass

    def get_best(self) -> Node:
        return None

    def is_closed(self, v: Node) -> bool:
        return True

    def is_opened(self, v: Node) -> bool:
        return True

    """
        G - a graph to search on 
        v_s - start node
        v_g - end_node
    """
    def search(self, graph: Graph, v_s: Node, v_g: Node, on_iteration, iteration_delay=0, slow_mo=False):
        self.init_open()
        v_s.g = 0
        v_s.h = self.h(v_s, v_g)
        v_s.prev = None
        self.open(v_s)
        iteration_counter = iteration_delay
        while self.get_open_size() > 0:
            current = self.get_best()
            if v_g == current:
                if on_iteration is not None:
                    on_iteration(self, graph)
                return current
            else:
                for v_n in current.neighbors:
                    if not self.is_closed(v_n) and not self.is_opened(v_n):
                        v_n.g = current.g + graph.cost(current, v_n)
                        v_n.h = self.h(v_n, v_g)
                        v_n.prev = current
                        self.open(v_n)
                self.close(current)
            if iteration_counter > 0:
                iteration_counter -= 1
            elif iteration_counter == 0:
                iteration_counter = iteration_delay
                on_iteration(self, graph)

            if slow_mo:
                time.sleep(0.001)

        on_iteration(self, graph)
        return None


