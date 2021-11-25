# Graphs
<!-- Short summary or background information -->

A graph is a non-linear kind of data structure made up of nodes or vertices and edges. The edges connect any two nodes in the graph, and the nodes are also known as vertices.

pull req: https://github.com/adhammhaydat/data-structures-and-algorithms401/pull/7

## Challenge
<!-- Description of the challenge -->
Implement your own Graph. The graph should be represented as an adjacency list

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Big o : 
1. time : O(n)
2. space : O(1)

## API
<!-- Description of each method publicly available in your Graph -->

1. add node
    * Arguments: value
    * Returns: The added node
    * Add a node to the graph
2. add edge
    * Arguments: 2 nodes to be connected by the edge, weight (optional)
    * Returns: nothing
    * Adds a new edge between two nodes in the graph
    * If specified, assign a weight to the edge
    * Both nodes should already be in the Graph
3. get nodes
    * Arguments: none
    * Returns all of the nodes in the graph as a collection (set, list, or similar)
4. get neighbors
    * Arguments: node
    * Returns a collection of edges connected to the given node
    * Include the weight of the connection in the returned collection
5. size
    * Arguments: none
    * Returns the total number of nodes in the graph
