# maze_generator

This software generates randomized 2D mazes. Each maze has a unique path from start (top left corner) to finish (bottmo right corner). The maze generation process is based on a graph data structure. For an N by N maze, we generate a graph with N^2 nodes, where each spot in the maze is a node. In the original graph, each node (row, column) is connected to all of its neighbores. We generate a spanning tree of this graph, which represents the maze.

To run this code, navigate to the src directory and run: 
```
python generator.py
```
or
```
python3 generator.py
```
