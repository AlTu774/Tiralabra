## Testing document
Testing can be done from terminal with the command:
```bash 
poetry run invoke test
```
## Coverage:
![Screenshot 2023-06-14 202642](https://github.com/AlTu774/Tiralabra/assets/81103520/fb219445-0dea-4100-8c64-9dacb987dbc7)

## Testing
Unit testing is done through pytest. Tile tests tests that the tiles(nodes) are connected correctly when taking into consideration the map's corners and the 8 branching directions from a node. There is also a simple test on the priority queue working. A* search is tested with the use of labyrinth like maps to see that the heuristic works properly. If A* works correctly, it can be used to test IDA* as well. In IDA* tests there is map where the starting point and end point are randomly picked, and if the lenght of the shortest path that IDA* finds matches the one that A* finds, then it passes the test. The IDA* test map is relatively small to make the testing faster.

The visual testing of the algorithms can be done on the visual interface of the project. If animation takes too long, it can be disabled by pressing the "a"-key.
