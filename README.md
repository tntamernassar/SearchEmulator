# Search Emulator

Simulates a search algorithm on a given image and save the simulation to GIF file.

It starts by letting the user draw a line between two pixels on the image which will be the start and the goal of the search algorithm.

Then simulating the given algorithm such that white pixels are the pixels that the algorithm can step on 

# **Usage:** 
  ````  
  SearchEmulator(gif_path='output.gif').emulate(image='image.png', algorithm=SearchAlgorithm())
  ```` 
  * **gif_path:** output gif simulation
  * **image:** input image with white pixels to simulate the search on 
  * **algorithm:** instance of ````SearchAlgorithm```` (check 'SearchAlgorithm' section)


  ***NOTICE: Only white pixels are reachable !***

<br />

# **Examples (Solving maze):**
  
  * **Heuristic Search (100 second)**
  ````  
  SearchEmulator(gif_path='../gifs/maze.gif').emulate(image='../mazes/maze.png', algorithm=Heuristic())
  ```` 
  https://user-images.githubusercontent.com/26690099/150878746-b4d419cf-82e5-48ed-8307-0353b7ce50d8.mp4


  <br /><br />
  * **BFS (432 seconds)**
  ````  
  SearchEmulator(gif_path='../gifs/maze.gif').emulate(image='../mazes/maze.png', algorithm=BFS())
  ```` 
  https://user-images.githubusercontent.com/26690099/150878677-f54fcbe8-1d54-4edd-82a6-259bca3a71be.mp4
  

  <br /><br />  
  * **DFS (178 seconds)**
  ````  
  SearchEmulator(gif_path='../gifs/maze.gif').emulate(image='../mazes/maze.png', algorithm=DFS())
  ```` 
  https://user-images.githubusercontent.com/26690099/150878646-8f8a73de-3117-4ef7-8588-1c01ce3f27e3.mp4


<br />

# **SearchAlgorithm:**

  Abstract Class representing a search algorithm.
  
  methods :
  
    - init_open: initialize open list
    
    - h: heuristic function 
    
    - open: open node
    
    - get_open_list: return opened nodes
    
    - get_open_size: return open nodes number
    
    - close: close node
    
    - get_close_list: return closed nodes
    
    - get_close_size: return closed nodes number
    
    - get_best: return best node 
    
    - is_closed: return true iff node is closed 
    
    - is_opened: return true iff node is opened
    
    - search: apply search algorithm
    
     
      search(G, vs, vg):
        init_open()
        vs.g = 0
        vs.h = h(vs, vg)
        vs.prev = null
        open(vs)
        while get_open_size() > 0:
          current = get_best()
          if vg == current
            return current
          else
            for vn in neighbors of current
              if vn is not closed and not opened
                vn.g = current.g + G.cost(current, vn) 
                vn.h = h(vn, vg)
                vn.prev = current
                open(vn)
            close(current)
            
        return null
        

    
      
