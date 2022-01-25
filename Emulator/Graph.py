import cv2
import threading
import random
import concurrent.futures
import imageio

LINE_FRAME_COUNTER = 10


class ImageHolder:
    def __init__(self, img: str):
        self.executor = concurrent.futures.ThreadPoolExecutor()
        self.frames = []

        self.original_img = cv2.imread(img)
        self.current_img = self.original_img.copy()
        self.height, self.width, self.channels = self.original_img.shape

        self.lining = False  # indicates if we are in drawing line state
        self.emulating = False  # indicates if we are in emulating state

        self.drawing = False
        self.line_frame_counter = LINE_FRAME_COUNTER
        self.start = (None, None)
        self.end = (None, None)

    def save_snapshot(self):
        self.frames.append(self.current_img.copy())

    def write_gif(self, gif_path):
        with imageio.get_writer(gif_path, mode='i') as writer:
            for frame in self.frames:
                writer.append_data(frame)

    def pixel(self, i, j):
        return self.current_img[i, j]

    def near_pixels(self, i, j):
        near = [
            (i, j + 1),  # right
            (i - 1, j),  # top
            (i + 1, j),  # bottom
            (i, j - 1),  # left
        ]

        _n = []
        for i in range(4):
            p = random.choice(near)
            near.remove(p)
            _n.append(p)

        return filter(lambda p: 0 <= p[0] < self.height and 0 <= p[1] < self.width, _n)

    def is_white(self, pixel):
        return pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255

    def make_draw_line_cb(self):
        def cb(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                self.drawing = True
                self.start = (y, x)

            elif event == cv2.EVENT_MOUSEMOVE:
                if self.drawing:
                    self.current_img = self.original_img.copy()
                    y1, x1 = self.start
                    cv2.line(self.current_img,
                                pt1=(x1, y1),
                                pt2=(x, y),
                                color=(0, 255, 0),
                                thickness=2)
                    if self.line_frame_counter == 0:
                        self.line_frame_counter = LINE_FRAME_COUNTER
                        self.save_snapshot()
                    else:
                        self.line_frame_counter -= 1

            elif event == cv2.EVENT_LBUTTONUP:
                self.end = (y, x)
                self.drawing = False
                self.lining = False
                self.current_img = self.original_img.copy()
        return cb

    def draw_line(self, cont, title="Draw a line"):
        def line_job():
            cv2.namedWindow(winname=title)
            cv2.setMouseCallback(title, self.make_draw_line_cb())

            while self.lining:
                cv2.imshow(title, self.current_img)
                cv2.waitKey(1)
            cv2.destroyAllWindows()
            cont(self.start, self.end)

        self.lining = True
        thread = threading.Thread(target=line_job)
        thread.start()

    def display(self, title="Emulator"):
        def job():
            cv2.namedWindow(winname=title)
            while self.emulating:
                cv2.imshow(title, self.current_img)
                cv2.waitKey(1)
            cv2.destroyAllWindows()

        self.emulating = True
        thread = threading.Thread(target=job)
        thread.start()

    def paint(self, pixels, color):
        for pixel in pixels:
            i, j = pixel
            self.current_img[i, j] = color


class Node:
    def __init__(self, name):
        self.name = name
        self.g = 0
        self.h = 0
        self.prev = None
        self.neighbors = []

    def get_neighbors(self):
        return self.neighbors

    def add_neighbor(self, node):
        self.neighbors.append(node)


class Graph:
    def __init__(self, img: str):
        self.nodes = {}  # node name, node instance
        self.edges = {}  # (node name, node name), cost
        self.image_holder = self.from_image(img)

    # creates a graph from image
    def from_image(self, img: str):
        image_holder = ImageHolder(img)
        for i in range(image_holder.height):
            for j in range(image_holder.width):
                name = (i, j)
                is_white = image_holder.is_white(image_holder.pixel(i, j))
                if is_white:
                    node = self.get_node(name)
                    near_pixels = image_holder.near_pixels(i, j)
                    for np in near_pixels:
                        if image_holder.is_white(image_holder.pixel(np[0], np[1])):
                            neighbor = self.get_node(np)
                            self.add_edge(node, neighbor)
        return image_holder

    def get_node(self, name):
        return self.nodes[name] if name in self.nodes else Node(name)

    def cost(self, v1: Node, v2: Node):
        e = (v1.name, v2.name)
        return self.edges[e]

    def add_edge(self, v1: Node, v2: Node):
        v1_name = v1.name
        v2_name = v2.name
        if v1_name not in self.nodes:
            self.nodes[v1_name] = v1
        if v2_name not in self.nodes:
            self.nodes[v2_name] = v2

        e = (v1_name, v2_name)
        self.edges[e] = 1
        v1.add_neighbor(v2)

    def set_edge_cost(self, v1: Node, v2: Node, cost: int):
        e = (v1.name, v2.name)
        self.edges[e] = cost

