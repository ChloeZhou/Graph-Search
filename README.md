# Graph-Search

# A delivery drone is an unmanned aerial vehicle(UAV) utilized to transport packages, food or other goods. In this programming assignment, we implement three kinds of search algorithms (Breadth-first search, Depth-first search, Uniform-cost search using the amount of fuel needed as cost) to deliver goods from a starting position S to a destination position D in an undirected weighted graph G.

# The drone has an initial amount of fuel, F, and cannot refill until it reaches the destination. The nodes in G represent the places where the drone can travel to. If an edge exists between node A and node B, the drone can travel from A to B. The weight of an edge corresponds to the amount of fuel needed to traverse that edge. So, the route selection will be restricted by the amount of fuel that the drone has. For example, when the drone is in node A, and there exists a path between A and B, the drone can go to B if and only if it has the necessary amount of fuel. Otherwise, B will be considered unreachable from A.

# If a path from S to D exists under the fuel constraint, the program will return the path; otherwise it will return “No Path”.
