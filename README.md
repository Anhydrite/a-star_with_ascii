# What is this?
This code is a basic A* algorithm implementation for finding the shortest path in a simple grid. The process is visualized in real time using an ASCII map.

# How does it work?
In the `main()` function, you define the *start* and *end* points. Calling `mapper.compute_path(start, end)` computes the path automatically.
The initial map is defined in `map_str`, which you can modify as needed.

## Symbol meanings
- `?`: unexplored cell
- `#`: impassable wall
- `-`: traversed cells
- `+`: final shortest path
