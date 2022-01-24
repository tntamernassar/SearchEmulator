from Emulator.Graph import Graph
from Emulator.SearchAlgorithm import SearchAlgorithm
import time

"""
    emulates the given search algorithm on the given image
    source and examples : https://github.com/tntamernassar/SearchEmulator
    
    Simulates a search algorithm on a given image and save the simulation to GIF file.
    It starts by letting the user draw a line between two pixels on the image
    which will be the start and the goal of the search algorithm.
    
    Then simulating the given algorithm such that white pixels are the pixels that the algorithm can step on.
    
    ############################################### Usage ###############################################
    #                                                                                                   #
    #    SearchEmulator(gif_path='output.gif').emulate(image='image.png', algorithm=SearchAlgorithm())  #
    #                                                                                                   #
    #       gif_path: output gif simulation                                                             #
    #       image: input image with white pixels to simulate the search on                              #
    #       algorithm: instance of SearchAlgorithm (check 'SearchAlgorithm' section)                    #
    #                                                                                                   #
    #####################################################################################################
    
        
                                    NOTICE: Only white pixels are reachable !
                                    
"""


class SearchEmulator:
    def __init__(self, gif_path=None):
        self.gif_path = gif_path

    @staticmethod
    def iteration_callback(algorithm: SearchAlgorithm, graph: Graph):
        open_list = algorithm.get_open_list()
        closed_list = algorithm.get_close_list()

        closed_list_pixels = map(lambda node: node.name, closed_list)
        graph.image_holder.paint(closed_list_pixels, [0, 0, 255])

        open_list_pixels = map(lambda node: node.name, open_list)
        graph.image_holder.paint(open_list_pixels, [0, 255, 0])
        graph.image_holder.save_snapshot()

    @staticmethod
    def paint_path(graph: Graph, path: list):
        path_pixels = map(lambda node: node.name, path)
        to_color_pixels = []
        for pixel in path_pixels:
            i, j = pixel
            near_pixels = graph.image_holder.near_pixels(i, j)
            to_color_pixels.append(pixel)
            to_color_pixels.extend(near_pixels)
        graph.image_holder.paint(to_color_pixels, [255, 0, 0])

    @staticmethod
    def display_emulator(graph: Graph, algo_name: str):
        graph.image_holder.display(title="Simulating " + algo_name + " Search")

    @staticmethod
    def extract_path(head) -> list:
        path = []
        current = head
        while current is not None:
            path.append(current)
            current = current.prev
        return list(reversed(path))

    @staticmethod
    def get_search_params(graph: Graph, cont):
        def _cont(start: (int, int), end: (int, int)):
            graph.image_holder.lining = False
            i1, j1 = start
            i2, j2 = end
            cont(graph.get_node((i1, j1)), graph.get_node((i2, j2)))

        graph.image_holder.draw_line(cont=_cont)

    def emulate(self, image: str, algorithm: SearchAlgorithm):
        print("Generating Graph from image")
        graph = Graph(image)
        print(len(graph.nodes), "Nodes generated")

        def _search(v_s, v_g):
            print(v_s.name, v_g.name)
            goal_pixles = [v_s.name, v_g.name]
            goal_pixles.extend(graph.image_holder.near_pixels(v_s.name[0], v_s.name[1]))
            goal_pixles.extend(graph.image_holder.near_pixels(v_g.name[0], v_g.name[1]))
            graph.image_holder.paint(goal_pixles, [0, 0, 0])
            self.display_emulator(graph, algorithm.name)
            start = time.time()
            dest = algorithm.search(graph, v_s=v_s, v_g=v_g, on_iteration=self.iteration_callback, iteration_delay=100, slow_mo=False)
            duration = time.time() - start
            print("Finished in", int(duration), "seconds")
            path = self.extract_path(dest)
            print("Path length:", len(path))
            self.paint_path(graph, path)
            for i in range(20):
                graph.image_holder.save_snapshot()
            if self.gif_path is not None:
                graph.image_holder.write_gif(self.gif_path)
        self.get_search_params(graph, cont=_search)


