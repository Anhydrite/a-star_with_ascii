# What is it ?
This code is a simple implementation of the A* algorithm within a simple problem of the shortest path. The whole is showed thanks to a realtime ASCII map.

# How does it work ?
In the `main()` method, you can create *end* and *start* point. Then call `mapper.compute_path(start, end)` and it will do the trick.
The initial is in map_str which can be edited freely.
Meanings of the signs:
* ? means undiscovered field
* \# is a direct wall which the player can't go through
* \- is a step (all cases that the player went on)
* \+ is the final shortest path when it has been found
